import pytest
import allure

from pages.android.login_page import LoginPage
from pages.android.home_page import HomePage
from pages.android.profile_selection import ProfileSelection
from utils.logger_utils import log
from pages.android.onboarding_page import OnboardingPage

@allure.feature("Authentication - Android")
class TestAndroidLoginSmoke:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_email_login_success(self, driver):
        log.info("🧪 test_email_login_success started")

        with allure.step("Navigate through onboarding"):
            onboarding = OnboardingPage(driver)
            onboarding.wait_for_onboarding()
            onboarding.tap_next()
            onboarding.tap_next()
            onboarding.tap_done()

        with allure.step("Wait for login screen"):
            login = LoginPage(driver)
            login.wait_for_login_screen()

        with allure.step("Enter valid credentials"):
            login.enter_email("buttercough3@gmail.com")
            login.enter_password("Password01!")

        with allure.step("Tap login button"):
            login.tap_login()

        with allure.step("Select a profile"):
            profile = ProfileSelection(driver)
            profile.wait_for_screen()
            profile.tap_profile_name("Angelo Budji")

        with allure.step("Verify home screen is displayed"):
            home = HomePage(driver)
            home.wait_for_home_screen()
            assert home.is_home_screen_visible(), \
                "❌ Home screen did not appear after valid login"

        log.info("✅ test_email_login_success passed")
