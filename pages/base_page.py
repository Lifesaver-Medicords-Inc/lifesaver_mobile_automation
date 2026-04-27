from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger_utils import log


class BasePage:
    TIMEOUT = 120

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, self.TIMEOUT)

    # ── Finders ───────────────────────────────────────────────────────────────

    def find(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator: tuple):
        self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    # ── Actions ───────────────────────────────────────────────────────────────

    def tap(self, locator: tuple):
        log.info(f"   Tapping → {locator[1]}")
        self.find_clickable(locator).click()

    def clear_and_type(self, locator: tuple, text: str):
        log.info(f"   Typing '{text}' → {locator[1]}")
        field = self.find_clickable(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text

    def is_enabled(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_enabled()
        except Exception:
            return False

    # ── Scroll ────────────────────────────────────────────────────────────────

    def scroll_down(self):
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=width  // 2,
            start_y=int(height * 0.8),
            end_x=width    // 2,
            end_y=int(height * 0.2),
            duration=800
        )
        log.info("   Scrolled down")

    def scroll_up(self):
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=width  // 2,
            start_y=int(height * 0.2),
            end_x=width    // 2,
            end_y=int(height * 0.8),
            duration=800
        )
        log.info("   Scrolled up")

    def swipe_left(self):
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=int(width * 0.8),
            start_y=height // 2,
            end_x=int(width * 0.2),
            end_y=height   // 2,
            duration=600
        )
        log.info("   Swiped left")

    def swipe_right(self):
        size   = self.driver.get_window_size()
        width  = size["width"]
        height = size["height"]
        self.driver.swipe(
            start_x=int(width * 0.2),
            start_y=height // 2,
            end_x=int(width * 0.8),
            end_y=height   // 2,
            duration=600
        )
        log.info("   Swiped right")

    # ── Keyboard ──────────────────────────────────────────────────────────────

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            log.info("   Keyboard hidden")
        except Exception:
            pass  # keyboard may already be hidden

    # ── Platform helpers ──────────────────────────────────────────────────────

    @property
    def platform(self) -> str:
        return self.driver.capabilities.get("platformName", "").lower()

    def is_ios(self) -> bool:
        return self.platform == "ios"

    def is_android(self) -> bool:
        return self.platform == "android"

    # ── Wait helpers ──────────────────────────────────────────────────────────

    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            log.info(f"   Element disappeared → {locator[1]}")
        except TimeoutException:
            log.warning(f"   Element still visible after {timeout}s → {locator[1]}")

    def wait_seconds(self, seconds: float):
        import time
        log.info(f"   Waiting {seconds}s...")
        time.sleep(seconds)