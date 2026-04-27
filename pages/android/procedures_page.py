from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from utils.logger_utils import log


class ProceduresPage(BasePage):

    # Locators

    # PROCEDURES LIST SCREEN
    # Header
    BACK_BUTTON       = (AppiumBy.ACCESSIBILITY_ID, 'Back')
    PROCEDURES_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Procedures"]')

    # Search & Filter
    SEARCH_BAR    = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Search..."]')
    FILTER_BUTTON = (AppiumBy.XPATH, '//android.view.View[@bounds="[592,193][688,289]"]')

    # Add Procedure Button
    ADD_PROCEDURE_BUTTON = (AppiumBy.XPATH, '//android.view.View[@content-desc="add_procedure_nav_btn"]')

    # Card 1 — Test Procedures from edit
    PROCEDURE_CARD_1          = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[1]')
    PROCEDURE_CARD_1_VIEW     = (AppiumBy.XPATH,  '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[1]/android.widget.Button[1]')
    PROCEDURE_CARD_1_EDIT     = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[1]/android.widget.Button[2]')
    PROCEDURE_CARD_1_DELETE   = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[1]/android.widget.Button[3]')
    PROCEDURE_CARD_1_DATE     = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Date")])[1]')
    PROCEDURE_CARD_1_DOCTOR   = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Doctor")])[1]')
    PROCEDURE_CARD_1_FLAGGED  = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Flagged")])[1]')
    PROCEDURE_CARD_1_PRIVATE  = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Private")])[1]')

    # Card 2 — Test Procedures from Modal
    PROCEDURE_CARD_2           = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[2]')
    PROCEDURE_CARD_2_VIEW      = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[2]/android.widget.Button[1]')
    PROCEDURE_CARD_2_EDIT      = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[2]/android.widget.Button[2]')
    PROCEDURE_CARD_2_DELETE    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[2]/android.widget.Button[3]')
    PROCEDURE_CARD_2_DATE      = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Date")])[2]')
    PROCEDURE_CARD_2_DOCTOR    = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Doctor")])[2]')
    PROCEDURE_CARD_2_FLAGGED   = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Flagged")])[2]')
    PROCEDURE_CARD_2_PRIVATE   = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Private")])[2]')

    # Card 3 — Herpes
    PROCEDURE_CARD_3           = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[3]')
    PROCEDURE_CARD_3_VIEW      = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[3]/android.widget.Button[1]')
    PROCEDURE_CARD_3_EDIT      = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[3]/android.widget.Button[2]')
    PROCEDURE_CARD_3_DELETE    = (AppiumBy.XPATH, '(//android.widget.ImageView[starts-with(@content-desc, "Title")])[3]/android.widget.Button[3]')
    PROCEDURE_CARD_3_DATE      = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Date")])[3]')
    PROCEDURE_CARD_3_DOCTOR    = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Doctor")])[3]')
    PROCEDURE_CARD_3_FLAGGED   = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Flagged")])[3]')
    PROCEDURE_CARD_3_PRIVATE   = (AppiumBy.XPATH, '(//android.view.View[starts-with(@content-desc, "Private")])[3]')

    # ADD PROCEDURE SCREEN
    # Header
    BACK_BUTTON           = (AppiumBy.ACCESSIBILITY_ID, 'Back')
    ADD_PROCEDURE_HEADER  = (AppiumBy.XPATH, '//android.view.View[@content-desc="Add Procedure"]')

    # Form - Labels
    REQUIRED_ASTERISK        = (AppiumBy.XPATH, '//android.view.View[@content-desc="*"]')
    TITLE_LABEL              = (AppiumBy.ACCESSIBILITY_ID, 'Title')
    DATE_TIME_LABEL          = (AppiumBy.ACCESSIBILITY_ID, 'Date & Time')
    DOCTOR_LABEL             = (AppiumBy.ACCESSIBILITY_ID, 'Doctor')
    PATIENTS_SIDENOTE_LABEL  = (AppiumBy.ACCESSIBILITY_ID, "Patient's Sidenote")
    DOCTORS_SIDENOTE_LABEL   = (AppiumBy.ACCESSIBILITY_ID, "Doctor's Sidenote")
    FILE_LABEL               = (AppiumBy.ACCESSIBILITY_ID, 'File')
    ATTACHMENTS_LABEL        = (AppiumBy.ACCESSIBILITY_ID, 'Attachments')
    FLAG_LABEL               = (AppiumBy.ACCESSIBILITY_ID, 'Flag')
    PRIVATE_LABEL            = (AppiumBy.ACCESSIBILITY_ID, 'Private')
    MAX_FILE_SIZE_LABEL      = (AppiumBy.ACCESSIBILITY_ID, 'Max file size : 8 mb')
    PRIVATE_WARNING_NOTE     = (AppiumBy.ACCESSIBILITY_ID,  'We recommend you to uncheck the private box because this information is important in an emergency.')

    # Form - Inputs (editable)
    TITLE_INPUT               = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Title"]')
    DATE_TIME_INPUT           = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Date & Time"]')
    DOCTOR_INPUT              = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Doctor"]')
    PATIENTS_SIDENOTE_INPUT   = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Enter Patient\'s Sidenote"]')
    FILE_UPLOAD_INPUT         = (AppiumBy.XPATH, '//android.widget.EditText[@text="Upload File"]')

    # Form - Read-only / Special
    DOCTORS_SIDENOTE_FIELD    = (AppiumBy.XPATH, '//android.view.View[@hint="This section can only be filled by your Doctor"]')  # disabled

    # Mic Buttons (beside inputs, no content-desc)
    TITLE_MIC_BUTTON               = (AppiumBy.XPATH, '//android.view.View[@bounds="[592,246][688,342]"]')
    DOCTOR_MIC_BUTTON              = (AppiumBy.XPATH, '//android.view.View[@bounds="[592,616][688,712]"]')
    PATIENTS_SIDENOTE_MIC_BUTTON   = (AppiumBy.XPATH, '//android.view.View[@bounds="[592,884][688,980]"]')

    # File Upload Actions
    FILE_UPLOAD_ICON      = (AppiumBy.XPATH, '//android.view.View[@bounds="[66,671][114,719]"]')
    FILE_CLEAR_BUTTON     = (AppiumBy.XPATH, '//android.view.View[@bounds="[474,671][522,719]"]')
    FILE_ACTION_BUTTON    = (AppiumBy.XPATH, '//android.view.View[@bounds="[572,633][688,757]"]')

    # Attachments
    ATTACH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Attach')

    # Toggles
    FLAG_TOGGLE     = (AppiumBy.XPATH, '//android.view.View[@bounds="[32,1091][80,1139]"]')
    PRIVATE_TOGGLE  = (AppiumBy.XPATH, '//android.view.View[@bounds="[32,1169][80,1217]"]')

    # Submit
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Add')

    # Scroll Container
    FORM_SCROLL_VIEW = (AppiumBy.XPATH, '//android.widget.ScrollView')

    # Confirm delete
    CONFIRM_DELETE = (AppiumBy.ACCESSIBILITY_ID, 'Yes')

    # Waits
    def wait_for_procedure_screen(self):
        log.info("Waiting for procedure screen...")
        self.find(self.PROCEDURES_HEADER)
        log.info("Procedure is open")

    def is_procedure_visible(self) -> bool:
        result = self.is_visible(self.PROCEDURES_HEADER)
        log.info(f"  Allergy screen visible: {result}")
        return result

    def wait_for_add_procedure_screen(self):
        log.info("Waiting for add procedure screen...")
        self.find(self.ADD_PROCEDURE_HEADER)
        log.info("Add procedure is open")

    def is_add_procedure_visible(self) -> bool:
        result = self.is_visible(self.ADD_PROCEDURE_HEADER)
        log.info(f"  Allergy screen visible: {result}")
        return result

    # Navigations
    def tap_add_procedure(self):
        log.info("Tap add procedure...")
        self.tap(self.ADD_PROCEDURE_BUTTON)

    def tap_back_button(self):
        log.info("Tap back button...")
        self.tap(self.BACK_BUTTON)

    # Actions
    def tap_delete_record(self):
        log.info(" tapping delete")
        self.tap(self.PROCEDURE_CARD_1_DELETE)
        log.info(f"  Delete record: {self.PROCEDURE_CARD_1_DELETE}")

    def tap_confirm_delete(self):
        log.info(" tapping confirm delete")
        self.tap(self.CONFIRM_DELETE)
        log.info(f"  Delete confirmed")


    def tap_save(self):
        log.info("Tap save...")
        self.tap(self.ADD_BUTTON)

    def enter_title(self, title: str):
        log.info("Enter title...")
        self.tap(self.TITLE_INPUT)
        self.clear_and_type(self.TITLE_INPUT, title)
        self.hide_keyboard()

    def enter_doctor_name(self, doctor_name: str):
        log.info("Enter doctor name...")
        self.tap(self.DOCTOR_INPUT)
        self.clear_and_type(self.DOCTOR_INPUT, doctor_name)
        self.hide_keyboard()

    def enter_patient_note(self, patient_note: str):
        log.info("Enter patient note...")
        self.tap(self.PATIENTS_SIDENOTE_INPUT)
        self.clear_and_type(self.PATIENTS_SIDENOTE_INPUT, patient_note)
        self.hide_keyboard()

    def create_patient_record(self, title: str, patient_note: str, doctor_name: str):
        log.info("Create patient record...")
        self.tap_add_procedure()
        self.wait_for_add_procedure_screen()
        self.enter_title(title)
        self.enter_doctor_name(doctor_name)
        self.enter_patient_note(patient_note)
        self.scroll_down()
        self.tap_save()
        self.wait_for_procedure_screen()

    # Assertions
    # def is_new_procedure_card_visible(self, title) -> bool:
    #     # should check if the frist index contains the title from input
    #     # locator = (AppiumBy.XPATH, f'(//android.widget.ImageView[starts-with(@content-desc, "Title")])[{index}]')
    #     locator = (AppiumBy.XPATH, f'//android.widget.ImageView[starts-with(@content-desc, "{title}")]')
    #     result = self.is_visible(locator)
    #     log.info(f'  Procedure card [{title}] visible: {result}')
    #     return result

    def is_new_procedure_card_visible(self, title: str) -> bool:
        # Get the first card and verify it contains the expected title
        first_card_locator = (
            AppiumBy.XPATH,
            '(//*[starts-with(@content-desc, "Title")])[1]'
        )
        try:
            first_card = self.find(first_card_locator)
            content_desc = first_card.get_attribute("content-desc")
            log.info(f'  First card content-desc: "{content_desc}"')

            result = title in content_desc
            log.info(f'  Expected title "{title}" found in first card: {result}')
            return result

        except Exception:
            return False