from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger_utils import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    # ── Locators ──────────────────────────────────────────────────────────────

    # Home Screen
    HOME_SCREEN               = (AppiumBy.XPATH, '//android.view.View[@content-desc="Home"]')
    SEARCH_BAR                = (AppiumBy.XPATH, '//android.widget.EditText')
    SEARCH_FILTER_BTN         = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[2]')
    NOTIFICATION_BELL         = (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[2]')

    # Patient Profiles Section
    PATIENT_PROFILES_HEADER   = (AppiumBy.ACCESSIBILITY_ID, 'Patient Profiles')
    PATIENT_PROFILES_SEE_ALL  = (AppiumBy.XPATH, '(//android.view.View[@content-desc="See All"])[1]')
    ADD_PATIENT_PROFILE_BTN   = (AppiumBy.ACCESSIBILITY_ID, '+')
    PATIENT_PROFILE_AVATAR_1  = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.view.View/android.widget.ImageView[1]')
    PATIENT_PROFILE_AVATAR_2  = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.view.View/android.widget.ImageView[2]')
    PATIENT_PROFILE_AVATAR_3  = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.view.View/android.widget.ImageView[3]')
    PATIENT_PROFILE_AVATAR_4  = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[5]/android.view.View/android.widget.ImageView[4]')
    PATIENT_PROFILE_D         = (AppiumBy.ACCESSIBILITY_ID, 'D')

    # Recent Records Section
    RECENT_RECORDS_HEADER     = (AppiumBy.ACCESSIBILITY_ID, 'Recent Records')
    RECENT_RECORDS_SEE_ALL    = (AppiumBy.XPATH, '(//android.view.View[@content-desc="See All"])[2]')
    RECENT_RECORD_CARD_1      = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Prescription\n30 March 2026\nTes prescription new data\nUnflagged\nNo data given"]')
    RECENT_RECORD_CARD_2      = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Prescription\n30 March 2026\nTest Prescription broken\nUnflagged\nNo data given"]')
    RECENT_RECORD_CARD_3      = (AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Prescription\n30 March 2026\nTest Prescription Creating new record\nFlagged\nNo data given"])[1]')

    # Active Records Section
    ACTIVE_RECORDS_HEADER     = (AppiumBy.ACCESSIBILITY_ID, 'Active Records')
    ACTIVE_RECORDS_SEE_ALL    = (AppiumBy.XPATH, '(//android.view.View[@content-desc="See All"])[3]')
    ACTIVE_RECORD_CARD_1      = (AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Prescription\n30 March 2026\nTest Prescription Creating new record\nFlagged\nNo data given"])[2]')
    ACTIVE_RECORD_CARD_2      = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Medical\n30 March 2026\nRealistic_Prescription.pdf\nFlagged\nNo data given"]')
    ACTIVE_RECORD_CARD_3      = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Vaccine\n30 March 2026\nTest Vaccine from Edit\nNo data given\nNo data given"]')

    # Navigation Bar
    HOME_NAV                  = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Home\nTab 1 of 5"]')
    DOCTORS_NAV               = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Doctors\nTab 2 of 5"]')
    RECORDS_NAV               = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Records\nTab 3 of 5"]')
    CARDS_NAV                 = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cards\nTab 4 of 5"]')
    PROFILE_NAV               = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Profile\nTab 5 of 5"]')

    # ── Waits ─────────────────────────────────────────────────────────────────

    def wait_for_home_screen(self):
        log.info("⏳ Waiting for home screen...")
        # self.find(self.HOME_SCREEN)
        WebDriverWait(self.driver, 120).until(
            EC.visibility_of_element_located(self.HOME_SCREEN)
        )
        log.info("✅ Home screen is visible")

    def is_home_screen_visible(self) -> bool:
        result = self.is_visible(self.HOME_SCREEN)
        log.info(f"   Home screen visible → {result}")
        return result

    # ── Navigation ────────────────────────────────────────────────────────────

    def go_to_home_nav(self):
        log.info("   Navigating to home screen")
        self.tap(self.HOME_NAV)

    def go_to_doctors_nav(self):
        log.info("   Navigating to doctors screen")
        self.tap(self.DOCTORS_NAV)

    def go_to_records_nav(self):
        log.info("   Navigating to Records nav")
        self.tap(self.RECORDS_NAV)

    def go_to_cards_nav(self):
        log.info("   Navigating to cards nav")
        self.tap(self.CARDS_NAV)

    def go_to_profile_nav(self):
        log.info("   Navigating to profile nav")
        self.tap(self.PROFILE_NAV)


    # ── Actions ───────────────────────────────────────────────────────────────

    # def tap_logout(self):
    #     log.info("   Tapping logout button")
    #     self.tap(self.LOGOUT_BUTTON)
    #     # handle confirmation dialog if present
    #     if self.is_visible(self.LOGOUT_CONFIRM, timeout=3):
    #         log.info("   Confirming logout dialog")
    #         self.tap(self.LOGOUT_CONFIRM)

    # ── Assertions ────────────────────────────────────────────────────────────

    # def get_welcome_message(self) -> str:
    #     text = self.get_text(self.WELCOME_MESSAGE)
    #     log.info(f"   Welcome message → {text}")
    #     return text
    #
    # def is_welcome_message_visible(self) -> bool:
    #     return self.is_visible(self.WELCOME_MESSAGE)
    #
    # def is_notifications_bell_visible(self) -> bool:
    #     return self.is_visible(self.NOTIFICATIONS_BELL)