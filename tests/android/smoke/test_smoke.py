import pytest
import allure

from conftest import driver, prescription_data
from pages.android.allergy_page import AllergyPage
from pages.android.procedures_page import ProceduresPage
from utils.logger_utils import log
from pages.android.home_page import HomePage
from pages.android.records_page import RecordsPage
from pytest_check import check

@allure.feature("Automated Smoke Testing - Android")
class TestAndroidSmoke:

    @allure.story("Full Smoke Cycle")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_smoke(self, logged_in_driver, allergy_data, procedure_data):
        log.info("🧪 test_smoke started")

        # Instances
        home       = HomePage(logged_in_driver)
        records    = RecordsPage(logged_in_driver)
        allergy    = AllergyPage(logged_in_driver)
        procedures = ProceduresPage(logged_in_driver)

        valid_allergy_record = allergy_data["valid"][0]
        valid_procedure_record = procedure_data["valid"][0]

        # Home Screen
        with allure.step("Login and verify home screen is displayed"):
            home.wait_for_home_screen()
            with check: assert home.is_home_screen_visible(), \
                "Home screen did not appear after valid login"
        log.info("Login test passed")

        # Records Screen
        with allure.step("Navigate to Records and verify screen"):
            home.go_to_records_nav()
            records.wait_for_record_screen()
            with check: assert records.is_record_screen_visible(), \
                "Records screen did not appear after tapping Record"
        log.info("Records navigation passed")

        # Allergy - Navigate
        with allure.step("Navigate to Allergy Category"):
            records.go_to_allergy()
            allergy.wait_for_allergy_screen()
            with check: assert allergy.is_allergy_screen_visible(), \
                "Allergy screen did not appear after tapping Allergy"
        log.info("Allergy navigation passed")

        # Allergy - Create
        # with allure.step("Create a new Allergy record"):
        #     allergy.create_allergy_record("Peanuts", "Rushes", "Dr. santos")
        # log.info("Create allergy passed")
        # Allergy - Create

        with allure.step("Create a new Allergy record"):
            allergy.create_allergy_record(
                allergy=valid_allergy_record["allergy"],
                reaction=valid_allergy_record["reaction"],
                doctor=valid_allergy_record["doctor_name"]
            )
        # Allergy - Verify
        with allure.step("Verify if the added allergy record is displayed"):
            allergy.wait_for_allergy_screen()
            with check: assert allergy.is_new_allergy_card_visible(title=valid_allergy_record["allergy"]), \
                "New allergy was not added to the list"
        log.info("Allergy record displayed")
        # Delete
        with allure.step("delete new added record"):
            allergy.tap_delete_record()
            allergy.tap_confirm_delete()
            allergy.wait_for_allergy_screen()
            allergy.tap_back_button()
            records.wait_for_record_screen()
            with check: assert not allergy.is_new_allergy_card_visible(title=valid_allergy_record["allergy"]), \
                "Allergy card was not deleted from the list"
        log.info("Successfully deleted record")


        # Procedures - Navigate
        with allure.step("Navigate to Procedures Category"):
            records.go_to_procedures()
            procedures.wait_for_procedure_screen()
            with check: assert procedures.is_procedure_visible(), \
                "Procedure screen did not appear after tapping Procedure"
        log.info("Procedures navigation passed")

        # Procedures - Create
        # with allure.step("Create a new Procedure record"):
        #     procedures.create_patient_record("LSD", "Take 3x a day for 3 weeks", "Dr. santos")
        # log.info("Create procedure passed")
        with allure.step("Create a new Procedure record"):
            procedures.create_patient_record(
                title=valid_procedure_record["title"],
                patient_note=valid_procedure_record["patient_sidenote"],
                doctor_name=valid_procedure_record["doctor_name"]
            )
        log.info("Create procedure passed")
        # Procedures - Verify
        with allure.step("Verify if the added procedure record is displayed"):
            procedures.wait_for_procedure_screen()
            with check: assert procedures.is_new_procedure_card_visible(title=valid_procedure_record["title"]), \
                "New procedure was not added to the list"
        log.info("Procedure record displayed")
        # Delete
        with allure.step("delete new added record"):
            procedures.tap_delete_record()
            procedures.tap_confirm_delete()
            procedures.wait_for_procedure_screen()
            # procedures.tap_back_button()
            # records.wait_for_record_screen()
            with check: assert not procedures.is_new_procedure_card_visible(title=valid_procedure_record["title"]), \
                "Procedure card was not deleted from the list"
        log.info("Successfully deleted record")


        # Navigate to Prescription
        # Create Prescription
        # View Prescription

        # Navigate to Vaccine
        # Create Vaccine
        # View Vaccine

        # Navigate to Medical Files
        # Create Medical Files
        # View Medical Files

        # Navigate to Expenses
        # Create Expenses
        # View Expenses


