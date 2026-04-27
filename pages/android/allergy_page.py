from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.logger_utils import log

class AllergyPage(BasePage):

    # Locators
    # Allergies Screen
    BACK_BUTTON          = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Back"]')
    ALLERGIES_HEADER     = (AppiumBy.XPATH, '//android.view.View[@content-desc="Allergies"]')
    SEARCH_BAR           = (AppiumBy.XPATH, '//android.widget.EditText')
    FILTER_BUTTON        = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    ADD_ALLERGY_BUTTON   = (AppiumBy.XPATH, '//android.view.View[@content-desc="add_allergy_nav_btn"]')

    # Card 1 — Peanuts (index="0")
    ALLERGY_CARD_1         = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[1]')
    ALLERGY_CARD_1_VIEW    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[1]/android.widget.Button[1]')
    ALLERGY_CARD_1_EDIT    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[1]/android.widget.Button[2]')
    ALLERGY_CARD_1_DELETE  = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[1]/android.widget.Button[3]')

    # Card 2 — Test Allergy from Modal (index="1")
    ALLERGY_CARD_2         = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[2]')
    ALLERGY_CARD_2_VIEW    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[2]/android.widget.Button[1]')
    ALLERGY_CARD_2_EDIT    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[2]/android.widget.Button[2]')
    ALLERGY_CARD_2_DELETE  = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[2]/android.widget.Button[3]')

    # Card 3 — ShortCut Module (index="2")
    ALLERGY_CARD_3         = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[3]')
    ALLERGY_CARD_3_VIEW    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[3]/android.widget.Button[1]')
    ALLERGY_CARD_3_EDIT    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[3]/android.widget.Button[2]')
    ALLERGY_CARD_3_DELETE  = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[3]/android.widget.Button[3]')

    # Add Allergy Screen - Header
    BACK_BUTTON        = (AppiumBy.ACCESSIBILITY_ID, 'Back')
    ADD_ALLERGY_HEADER = (AppiumBy.ACCESSIBILITY_ID, 'Add Allergy')

    # Form - Labels
    CATEGORY_LABEL           = (AppiumBy.ACCESSIBILITY_ID, 'Category')
    ALLERGY_LABEL            = (AppiumBy.ACCESSIBILITY_ID, 'Allergy')
    DATE_LABEL               = (AppiumBy.ACCESSIBILITY_ID, 'Date')
    SEVERITY_LABEL           = (AppiumBy.ACCESSIBILITY_ID, 'Severity')
    REACTION_LABEL           = (AppiumBy.ACCESSIBILITY_ID, 'Reaction')
    PATIENTS_SIDENOTE_LABEL  = (AppiumBy.ACCESSIBILITY_ID, "Patient's Sidenote")
    DOCTOR_LABEL             = (AppiumBy.ACCESSIBILITY_ID, 'Doctor')
    DOCTORS_SIDENOTE_LABEL   = (AppiumBy.ACCESSIBILITY_ID, "Doctor's Sidenote")
    ATTACHMENTS_LABEL        = (AppiumBy.ACCESSIBILITY_ID, 'Attachments')
    FLAG_LABEL               = (AppiumBy.ACCESSIBILITY_ID, 'Flag')
    PRIVATE_LABEL            = (AppiumBy.ACCESSIBILITY_ID, 'Private')

    # Form - Inputs (editable)
    CATEGORY_DROPDOWN        = (AppiumBy.ACCESSIBILITY_ID, 'Food Allergy')
    ALLERGY_INPUT            = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Allergy"]')
    DATE_INPUT               = (AppiumBy.XPATH, '//android.widget.EditText[@hint="MM/DD/YYYY"]')
    SEVERITY_DROPDOWN        = (AppiumBy.ACCESSIBILITY_ID, 'Mild')
    REACTION_INPUT           = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Reaction"]')
    PATIENTS_SIDENOTE_INPUT  = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Patient\'s Sidenote"]')
    DOCTOR_INPUT             = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Doctor"]')

    # Form - Read-only / Special
    DOCTORS_SIDENOTE_FIELD = (AppiumBy.XPATH, '//android.view.View[@hint="This section can only be filled by your Doctor"]')  # disabled

    # Toggles
    FLAG_TOGGLE     = (AppiumBy.XPATH, '//android.view.View[@content-desc="Flag"]/preceding-sibling::android.view.View[1]')
    PRIVATE_TOGGLE  = (AppiumBy.XPATH, '//android.view.View[@content-desc="Private"]/preceding-sibling::android.view.View[1]')

    # Attachments
    ATTACH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Attach')

    # Submit
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Add')

    # COnfirm delete
    CONFIRM_DELETE = (AppiumBy.ACCESSIBILITY_ID, 'Yes')
    # Wait
    def wait_for_allergy_screen(self):
        log.info(" waiting for allergy screen")
        self.find(self.ALLERGIES_HEADER)
        log.info(" Allergy screen is open...")

    def is_allergy_screen_visible(self) -> bool:
        result = self.is_visible(self.ALLERGIES_HEADER)
        log.info(f"  Allergy screen visible: {result}")
        return result

    def wait_for_add_allergy_screen(self):
        log.info("  waiting for add allergy screen")
        self.find(self.ADD_ALLERGY_HEADER)
        log.info("  Add allergy screen is open...")

    def is_new_added_allergy_visible(self) -> bool:
        result = self.is_visible(self.ALLERGY_CARD_1)
        self.find(self.ALLERGY_CARD_1)
        log.info(f"  New allergy is visible: {result}")
        return result


    # Navigations
    def tap_add_allergy(self):
        log.info(" tapping add allergy")
        self.tap(self.ADD_ALLERGY_BUTTON)
    def tap_back_button(self):
        log.info("  tapping back button")
        self.tap(self.BACK_BUTTON)

    # Actions
    def enter_allergy(self, allergy: str):
        self.tap(self.ALLERGY_INPUT)
        log.info(f"  enter allergy: {allergy}")
        self.clear_and_type(self.ALLERGY_INPUT, allergy)
        self.hide_keyboard()

    def enter_reaction(self, reaction: str):
        self.tap(self.REACTION_INPUT)
        log.info(f"  enter reaction: {reaction}")
        self.clear_and_type(self.REACTION_INPUT, reaction)
        self.hide_keyboard()

    def enter_doctor(self, doctor: str):
        self.tap(self.DOCTOR_INPUT)
        log.info(f"  enter doctor: {doctor}")
        self.clear_and_type(self.DOCTOR_INPUT, doctor)
        self.hide_keyboard()

    def tap_save(self):
        log.info(" tapping save")
        self.tap(self.ADD_BUTTON)

    def create_allergy_record(self, allergy: str, reaction: str ,doctor: str):
        log.info(f"Creating allergy record: {allergy}")
        self.tap_add_allergy()
        self.wait_for_add_allergy_screen()
        self.enter_allergy(allergy)
        self.enter_reaction(reaction)
        self.scroll_down()
        self.enter_doctor(doctor)
        self.scroll_down()
        self.tap_save()
        self.wait_for_allergy_screen()

    def tap_delete_record(self):
        log.info(" tapping delete")
        self.tap(self.ALLERGY_CARD_1_DELETE)
        log.info(f"  Delete record: {self.ALLERGY_CARD_1_DELETE}")

    def tap_confirm_delete(self):
        log.info(" tapping confirm delete")
        self.tap(self.CONFIRM_DELETE)
        log.info(f"  Delete confirmed")


    # Assertions
    # def is_new_allergy_card_visible(self, index: int = 1) -> bool:
    #     locator = (AppiumBy.XPATH, f'(//android.widget.ImageView[starts-with(@content-desc, "Allergy")])[{index}]')
    #     result = self.is_visible(locator)
    #     log.info(f'  Allergy card [{index}] visible: {result}')
    #     return result

    def is_new_allergy_card_visible(self, title: str) -> bool:
        # Get the first card and verify it contains the expected title
        first_card_locator = (
            AppiumBy.XPATH,
            '(//*[starts-with(@content-desc, "Allergy")])[1]'
        )
        try:
            first_card = self.find(first_card_locator)
            content_desc = first_card.get_attribute("content-desc")
            log.info(f'  First card content-desc: "{content_desc}"')

            result = title in content_desc
            log.info(f'  Expected title "{title}" found in first card: {result}')
            return result

        except Exception as e:
            log.warning(f'  Could not find first procedure card: {e}')
            return False

