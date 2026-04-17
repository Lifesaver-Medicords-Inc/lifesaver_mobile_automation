import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver

from config.android_caps import android_server, android_caps
from config.ios_caps import ios_server, ios_caps
from utils.logger_utils import log, on_failure


# ── CLI option ───────────────────────────────────────────────────────────────

def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="ios",
        choices=["android", "ios"],
        help="Target platform to run tests on: ios | android",
    )

# ── Session-scoped: read once for the whole run ──────────────────────────────

@pytest.fixture(scope="session")
def platform(request):
    value = request.config.getoption("--platform")
    log.info(f"🖥️  Platform selected → {value.upper()}")
    return value

# ── Module-scoped: one driver per test file ──────────────────────────────────

@pytest.fixture(scope="module")
def driver(platform):
    if platform == "ios":
        server  = ios_server
        options = XCUITestOptions().load_capabilities(ios_caps)
        device  = ios_caps["appium:deviceName"]
        udid    = ios_caps["appium:udid"]
    else:
        server  = android_server
        options = UiAutomator2Options().load_capabilities(android_caps)
        device  = android_caps["appium:deviceName"]
        udid    = android_caps["appium:udid"]

    log.info("🚀 Starting Appium session...")
    log.info(f"   Platform → {platform.upper()}")
    log.info(f"   Server   → {server}")
    log.info(f"   Device   → {device}")
    log.info(f"   UDID     → {udid}")

    drv = webdriver.Remote(server, options=options)
    log.info(f" Session started │ ID: {drv.session_id}")

    yield drv

    log.info(" Tearing down session...")
    drv.quit()
    log.info(" Session closed.")


# ── Function-scoped: logged-in driver ────────────────────────────────────────

@pytest.fixture(scope="function")
def logged_in_driver(driver, platform):
    if platform == "ios":
        from pages.ios.login_page import LoginPage
    else:
        from pages.android.login_page import LoginPage

    login = LoginPage(driver)
    login.login("buttercough3@gmail.com", "Password01!")
    yield driver
    login.logout()


# ── Auto-skip tests marked for a specific platform ───────────────────────────

@pytest.fixture(autouse=True)
def skip_by_platform(request, platform):
    marker = request.node.get_closest_marker("platform")
    if marker:
        allowed = marker.args[0]
        if platform != allowed:
            pytest.skip(f" Skipped — test only runs on {allowed.upper()}")


# ── Capture screenshot + logs on failure ─────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            on_failure(drv, test_name=item.name)
        log.error(f" FAILED │ {item.name}")

    elif report.when == "call" and report.passed:
        log.info(f" PASSED │ {item.name}")