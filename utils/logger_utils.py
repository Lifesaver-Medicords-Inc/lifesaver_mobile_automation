import logging
import os
from datetime import datetime

import allure
import pytest

# ── Log directory setup ──────────────────────────────────────────────────────

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILENAME = os.path.join(
    LOG_DIR,
    f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# ── Formatter ────────────────────────────────────────────────────────────────

FORMATTER = logging.Formatter(
    fmt="%(asctime)s │ %(levelname)-8s │ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ── Handlers ─────────────────────────────────────────────────────────────────

# Console handler — shows logs in terminal during test run
_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.DEBUG)
_console_handler.setFormatter(FORMATTER)

# File handler — saves logs to logs/test_run_YYYYMMDD_HHMMSS.log
_file_handler = logging.FileHandler(LOG_FILENAME, encoding="utf-8")
_file_handler.setLevel(logging.DEBUG)
_file_handler.setFormatter(FORMATTER)

# ── Logger ───────────────────────────────────────────────────────────────────

log = logging.getLogger("AppiumTests")
log.setLevel(logging.DEBUG)
log.addHandler(_console_handler)
log.addHandler(_file_handler)

# prevent duplicate logs if pytest captures logging too
log.propagate = False

# ── Screenshot on failure ────────────────────────────────────────────────────

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def on_failure(driver, test_name: str = "unknown"):
    """
    Called when a test fails.
    - Takes a screenshot
    - Saves it to screenshots/
    - Attaches it to the Allure report
    - Attaches the device log (logcat / syslog) to Allure
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name  = test_name.replace(" ", "_").replace("/", "-")
    filename   = f"{safe_name}_{timestamp}.png"
    filepath   = os.path.join(SCREENSHOT_DIR, filename)

    # ── Screenshot ───────────────────────────────────────────────────────────
    try:
        driver.save_screenshot(filepath)
        log.info(f"📸 Screenshot saved → {filepath}")

        with open(filepath, "rb") as f:
            allure.attach(
                f.read(),
                name=f"FAIL: {test_name}",
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        log.warning(f"⚠️  Could not take screenshot: {e}")

    # ── Device log (logcat for Android / syslog for iOS) ─────────────────────
    try:
        # Appium returns the appropriate log type per platform
        log_type = _detect_log_type(driver)
        if log_type:
            device_logs = driver.get_log(log_type)
            log_text    = "\n".join(
                f"[{entry['level']}] {entry['message']}"
                for entry in device_logs
            )
            allure.attach(
                log_text,
                name=f"Device Log: {test_name}",
                attachment_type=allure.attachment_type.TEXT
            )
            log.info(f"📋 Device log ({log_type}) attached to Allure")
    except Exception as e:
        log.warning(f"⚠️  Could not capture device log: {e}")

    # ── Page source (XML dump of current screen) ──────────────────────────────
    try:
        page_source = driver.page_source
        allure.attach(
            page_source,
            name=f"Page Source: {test_name}",
            attachment_type=allure.attachment_type.XML
        )
        log.info("📄 Page source attached to Allure")
    except Exception as e:
        log.warning(f"⚠️  Could not capture page source: {e}")


def _detect_log_type(driver) -> str | None:
    """
    Returns the correct Appium log type string based on platform.
    Returns None if it can't be determined.
    """
    try:
        platform = driver.capabilities.get("platformName", "").lower()
        if platform == "android":
            return "logcat"
        elif platform == "ios":
            return "syslog"
    except Exception:
        pass
    return None