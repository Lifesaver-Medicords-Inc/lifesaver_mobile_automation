import allure
import pytest

from pages.android.home_page import HomePage
from pages.android.records_page import RecordsPage
from utils.logger_utils import log


@allure.feature("Create Prescription - Android")
class TestCreatePrescription:

    @allure.story("Create Prescription")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_create_prescription(self, logged_in_driver):
        log.info("Create Prescription")

        with allure.step("Navigate to Records Page"):
            home = HomePage(logged_in_driver)
            home.wait_for_home_screen()
            home.go_to_records_nav()

        with allure.step("Open Prescription Page"):
            records = RecordsPage(logged_in_driver)
            records.wait_for_record_screen()
            records.go_to_prescription()

        # with allure.step("Tap Add button"):
        #
        # with allure.step("Fill up required fields"):
        #
        # with allure.step("Tap Submit"):
        #
        # # Since its smoke no need to validate
        # # check if need to browse if it was added