from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger_utils import log


class HomePage(BasePage):

    # ── Locators ──────────────────────────────────────────────────────────────
    # ⚠️  Replace values with your actual app's element IDs / xpaths

    HOME_SCREEN        = (AppiumBy.ACCESSIBILITY_ID, "home_screen")
    PROFILE_TAB        = (AppiumBy.ACCESSIBILITY_ID, "profile_tab")
    LOGOUT_BUTTON      = (AppiumBy.ACCESSIBILITY_ID, "logout_button")
    LOGOUT_CONFIRM     = (AppiumBy.ACCESSIBILITY_ID, "logout_confirm_button")
    WELCOME_MESSAGE    = (AppiumBy.ACCESSIBILITY_ID, "welcome_message")
    NOTIFICATIONS_BELL = (AppiumBy.ACCESSIBILITY_ID, "notifications_bell")
    SETTINGS_ICON      = (AppiumBy.ACCESSIBILITY_ID, "settings_icon")

    # ── Waits ─────────────────────────────────────────────────────────────────

    def wait_for_home_screen(self):
        log.info("⏳ Waiting for home screen...")
        self.find(self.HOME_SCREEN)
        log.info("✅ Home screen is visible")

    def is_home_screen_visible(self) -> bool:
        result = self.is_visible(self.HOME_SCREEN)
        log.info(f"   Home screen visible → {result}")
        return result

    # ── Navigation ────────────────────────────────────────────────────────────

    def go_to_profile(self):
        log.info("   Navigating to profile tab")
        self.tap(self.PROFILE_TAB)

    def go_to_settings(self):
        log.info("   Navigating to settings")
        self.tap(self.SETTINGS_ICON)

    def go_to_notifications(self):
        log.info("   Navigating to notifications")
        self.tap(self.NOTIFICATIONS_BELL)

    # ── Actions ───────────────────────────────────────────────────────────────

    def tap_logout(self):
        log.info("   Tapping logout button")
        self.tap(self.LOGOUT_BUTTON)
        # handle confirmation dialog if present
        if self.is_visible(self.LOGOUT_CONFIRM, timeout=3):
            log.info("   Confirming logout dialog")
            self.tap(self.LOGOUT_CONFIRM)

    # ── Assertions ────────────────────────────────────────────────────────────

    def get_welcome_message(self) -> str:
        text = self.get_text(self.WELCOME_MESSAGE)
        log.info(f"   Welcome message → {text}")
        return text

    def is_welcome_message_visible(self) -> bool:
        return self.is_visible(self.WELCOME_MESSAGE)

    def is_notifications_bell_visible(self) -> bool:
        return self.is_visible(self.NOTIFICATIONS_BELL)