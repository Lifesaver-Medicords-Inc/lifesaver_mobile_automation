
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from utils.logger_utils import log


class RecordsPage(BasePage):

    # ── Locators ──────────────────────────────────────────────────────────────

    # Records Screen
    RECORDS_SCREEN        = (AppiumBy.XPATH, '(//android.view.View[@content-desc="Records"])[1]')
    NOTIFICATION_BELL     = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]')

    # Category Section
    CATEGORY_HEADER       = (AppiumBy.ACCESSIBILITY_ID, 'Category')
    ALLERGY               = (AppiumBy.ACCESSIBILITY_ID, 'Allergy')
    DIAGNOSIS             = (AppiumBy.ACCESSIBILITY_ID, 'Diagnosis')
    INSURANCE             = (AppiumBy.ACCESSIBILITY_ID, 'Insurance')
    PROCEDURES            = (AppiumBy.ACCESSIBILITY_ID, 'Procedures')
    ORGAN_DONATIONS       = (AppiumBy.ACCESSIBILITY_ID, 'Organ Donations')
    PRESCRIPTIONS         = (AppiumBy.ACCESSIBILITY_ID, 'Prescriptions')
    VACCINES              = (AppiumBy.ACCESSIBILITY_ID, 'Vaccines')
    MEDICAL_FILES         = (AppiumBy.ACCESSIBILITY_ID, 'Medical Files')
    EXPENSES              = (AppiumBy.ACCESSIBILITY_ID, 'Expenses')
    INVOICES              = (AppiumBy.ACCESSIBILITY_ID, 'Invoices')
    MEDICAL_HISTORY       = (AppiumBy.ACCESSIBILITY_ID, 'Medical History')
    DOCTORS_NOTES         = (AppiumBy.ACCESSIBILITY_ID, "Doctor's Notes")
    PREVIEW               = (AppiumBy.ACCESSIBILITY_ID, 'Preview')
    NOTE                  = (AppiumBy.ACCESSIBILITY_ID, 'Note')

    # Records Section
    RECORDS_HEADER        = (AppiumBy.XPATH, '(//android.view.View[@content-desc="Records"])[2]')
    FLAGGED_RECORD        = (AppiumBy.ACCESSIBILITY_ID, 'Flagged Record')
    PRIVATE_RECORDS       = (AppiumBy.ACCESSIBILITY_ID, 'Private Records')

    # Navigation Bar
    HOME_NAV              = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Home\nTab 1 of 5"]')
    DOCTORS_NAV           = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Doctors\nTab 2 of 5"]')
    RECORDS_NAV           = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Records\nTab 3 of 5"]')
    CARDS_NAV             = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cards\nTab 4 of 5"]')
    PROFILE_NAV           = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Profile\nTab 5 of 5"]')

    # ── Waits ─────────────────────────────────────────────────────────────────
    def wait_for_record_screen(self):
        log.info("Waiting for record screen...")
        self.find(self.RECORDS_SCREEN)
        log.info("Record screen is open...")

    def is_record_screen_visible(self) -> bool:
        result = self.is_visible(self.RECORDS_SCREEN)
        log.info(f"   Record screen visible → {result}")
        return result

    # ── Navigation ────────────────────────────────────────────────────────────
    def go_to_allergy(self):
        log.info("Tap allergy...")
        self.tap(self.ALLERGY)

    def get_error_message(self):
        self.get_text(self.ALLERGY)

    def go_to_procedures(self):
        log.info("Tap procedures...")
        self.tap(self.PROCEDURES)

    def go_to_prescription(self):
        log.info("Tap prescription...")
        self.tap(self.PRESCRIPTIONS)

    def go_to_vaccines(self):
        log.info("Tap vaccines...")
        self.tap(self.VACCINES)

    def go_to_medical_files(self):
        log.info("Tap medical files...")
        self.tap(self.MEDICAL_FILES)

    def go_to_expenses(self):
        log.info("Tap expenses...")
        self.tap(self.EXPENSES)


    # ── Actions ───────────────────────────────────────────────────────────────


    # ── Assertions ────────────────────────────────────────────────────────────
