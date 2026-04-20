from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from utils.logger_utils import log

class OnboardingPage(BasePage):

    def __init__(self,driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver,self.TIMEOUT)

    # ── Locators ──────────────────────────────────────────────────────────────
    PAGE1_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Helping You Keep Track of Everything')
    PAGE2_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Track Your Medical Record Instantly')
    PAGE3_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Set Your Record to Private or Flag & make it a Priority')
    NEXT_BTN    = (AppiumBy.ACCESSIBILITY_ID, 'Next')
    DONE_BTN    = (AppiumBy.ACCESSIBILITY_ID, 'Done')

    # ── Waits ─────────────────────────────────────────────────────────────────
    def wait_for_onboarding(self):
        log.info("Waiting for onboarding screen...")
        self.find(self.PAGE1_TITLE)
        log.info("Onboarding screen visible")

    # ── Getters ───────────────────────────────────────────────────────────────
    def get_page_title(self, locator) -> str:
        self.find(locator)
        return self.get_text(locator)

    # ── Actions ───────────────────────────────────────────────────────────────
    def tap_next(self):
        log.info("   Tapping Next")
        self.tap(self.NEXT_BTN)

    def tap_done(self):
        log.info("   Tapping Done")
        self.tap(self.DONE_BTN)
