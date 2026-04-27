from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.logger_utils import log


class ProfileSelection(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    # ── Locators ──────────────────────────────────────────────────────────────
    TITLE_PAGE          = (AppiumBy.ACCESSIBILITY_ID, "Select Profile")
    ALL_PROFILES        = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc]')
    ADD_PROFILE_BTN     = (AppiumBy.XPATH, "//android.widget.Button")

    # ── Waits ─────────────────────────────────────────────────────────────────
    def wait_for_screen(self):
        log.info("   Waiting for Select Profile screen")
        self.find(self.TITLE_PAGE)
        log.info("   Select Profile screen visible")

    # ── Getters ───────────────────────────────────────────────────────────────
    def get_all_profiles(self) -> list:
        log.info("   Getting all profiles")
        profiles = self.find(self.ALL_PROFILES)
        return [p.get_attribute("content-desc") for p in profiles]

    # ── Actions ───────────────────────────────────────────────────────────────
    def tap_profile_name(self, name: str):
        log.info(f"   Tap profile name: {name}")
        # locator = (AppiumBy.XPATH, f'//*[contains(@content-desc, "{name}")]')
        locator = (AppiumBy.XPATH, f'//android.widget.ImageView[@content-desc="{name}"]')
        self.tap(locator)

    def tap_add_profile(self):
        log.info(f"   Tap add profile button")
        self.tap(self.ADD_PROFILE_BTN)



