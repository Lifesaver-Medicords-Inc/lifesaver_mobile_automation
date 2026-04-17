import pytest
import allure

from pages.android.login_page import LoginPage
from pages.android.home_page import HomePage
from utils.logger_utils import log


@allure.feature("Authentication - Android")
class TestAndroidLoginSmoke:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_email_login_success(self, driver):
        log.info("🧪 test_email_login_success started")

        with allure.step("Wait for login screen"):
            login = LoginPage(driver)
            login.wait_for_login_screen()

        with allure.step("Enter valid credentials"):
            login.enter_email("buttercough3@gmail.com")
            login.enter_password("Password01!")

        with allure.step("Tap login button"):
            login.tap_login()

        with allure.step("Verify home screen is displayed"):
            home = HomePage(driver)
            assert home.is_home_screen_visible(), \
                "❌ Home screen did not appear after valid login"

        log.info("✅ test_email_login_success passed")
