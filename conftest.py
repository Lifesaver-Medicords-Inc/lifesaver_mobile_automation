import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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
    parser.addoption(
        "--test-type",
        action="store",
        default="smoke",
        choices=["smoke", "regression"],
        help="Test type: smoke | regression",
    )

# ── Session-scoped: read once for the whole run ──────────────────────────────

@pytest.fixture(scope="session")
def platform(request):
    value = request.config.getoption("--platform")
    log.info(f"Platform selected → {value.upper()}")
    return value

@pytest.fixture(scope="session")
def no_reset(request):
    test_type = request.config.getoption("--test-type")
    value = test_type == "regression"
    log.info(f"Test type → {test_type.upper()} │ noReset → {value}")
    return value

# ── Module-scoped: one driver per test file ──────────────────────────────────

def wait_for_app_ready(driver):
    WebDriverWait(driver, 30).until(
        lambda d: d.page_source is not None and len(d.page_source) > 1500
    )

@pytest.fixture(scope="module")
def driver(platform, no_reset):
    if platform == "ios":
        server  = ios_server
        caps    = {**ios_caps, "appium:noReset": no_reset}
        options = XCUITestOptions().load_capabilities(caps)
        device  = ios_caps["appium:deviceName"]
        udid    = ios_caps["appium:udid"]
    else:
        server  = android_server
        caps = {**android_caps, "appium:noReset": no_reset}
        options = UiAutomator2Options().load_capabilities(caps)
        device  = android_caps["appium:deviceName"]
        udid    = android_caps["appium:udid"]

    log.info("🚀 Starting Appium session...")
    log.info(f"   Platform → {platform.upper()}")
    log.info(f"   Server   → {server}")
    log.info(f"   Device   → {device}")
    log.info(f"   UDID     → {udid}")
    log.info(f"   noReset  → {no_reset}")

    drv = webdriver.Remote(server, options=options)
    drv.implicitly_wait(0)
    log.info(f" Session started │ ID: {drv.session_id}")

    wait_for_app_ready(drv)

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
        from pages.android.onboarding_page import OnboardingPage
        from pages.android.login_page import LoginPage
        from pages.android.profile_selection import ProfileSelection

    # Onboarding
    onboarding = OnboardingPage(driver)
    onboarding.wait_for_onboarding()
    onboarding.tap_next()
    onboarding.tap_next()
    onboarding.tap_done()

    # Login
    login = LoginPage(driver)
    login.wait_for_login_screen()
    login.login("buttercough3@gmail.com", "Password01!")

    # Select Profile
    profile = ProfileSelection(driver)
    profile.wait_for_screen()
    profile.tap_profile_name("Angelo Budji")

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