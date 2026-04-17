from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger_utils import log


class LoginPage(BasePage):

    # ── Locators ──────────────────────────────────────────────────────────────
    # ⚠️  Replace values with your actual app's element IDs / xpaths

    # Common (iOS + Android)
    LOGIN_SCREEN         = (AppiumBy.XPATH, '//*[@text="Welcome Back,"]')
    EMAIL_FIELD          = (AppiumBy.XPATH, '//*[@text="Enter Email"]')
    PASSWORD_FIELD       = (AppiumBy.XPATH, '//*[@text="Enter Password"]')
    LOGIN_BUTTON         = (AppiumBy.XPATH, '//*[@text="Login"]')
    FORGOT_PASSWORD_LINK = (AppiumBy.XPATH, '//*[@text="Forgot Password"]')
    REQUIRED_FIELD_ERROR = (AppiumBy.XPATH, '//*[@text="Required field"]')
    ERROR_MESSAGE        = (AppiumBy.XPATH, '//*[contains(@text,"Invalid") or contains(@text,"incorrect") or contains(@text,"Wrong")]')

    # Forgot password screen
    FORGOT_PASSWORD_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "forgot_password_screen")
    RESET_EMAIL_FIELD      = (AppiumBy.ACCESSIBILITY_ID, "reset_email_input")
    SEND_RESET_BUTTON      = (AppiumBy.ACCESSIBILITY_ID, "send_reset_button")
    RESET_CONFIRMATION     = (AppiumBy.ACCESSIBILITY_ID, "reset_confirmation_message")

    # iOS only
    FACE_ID_BUTTON         = (AppiumBy.ACCESSIBILITY_ID, "face_id_button")

    # Android only
    FINGERPRINT_BUTTON     = (AppiumBy.ACCESSIBILITY_ID, "fingerprint_button")

    # ── Waits ─────────────────────────────────────────────────────────────────

    def wait_for_login_screen(self):
        log.info("⏳ Waiting for login screen...")
        self.find(self.LOGIN_SCREEN)
        log.info("✅ Login screen is visible")

    def is_login_screen_visible(self) -> bool:
        return self.is_visible(self.LOGIN_SCREEN)

    # ── Actions ───────────────────────────────────────────────────────────────

    def enter_email(self, email: str):
        log.info(f"   Entering email → {email or '(empty)'}")
        self.clear_and_type(self.EMAIL_FIELD, email)

    def enter_password(self, password: str):
        log.info("   Entering password → ****")
        self.clear_and_type(self.PASSWORD_FIELD, password)

    def tap_login(self):
        log.info("   Tapping login button")
        self.hide_keyboard()
        self.tap(self.LOGIN_BUTTON)

    def tap_forgot_password(self):
        log.info("   Tapping forgot password link")
        self.tap(self.FORGOT_PASSWORD_LINK)

    def enter_reset_email(self, email: str):
        log.info(f"   Entering reset email → {email}")
        self.clear_and_type(self.RESET_EMAIL_FIELD, email)

    def tap_send_reset_link(self):
        log.info("   Tapping send reset link button")
        self.tap(self.SEND_RESET_BUTTON)

    # ── iOS biometric ─────────────────────────────────────────────────────────

    def tap_face_id_button(self):
        log.info("   Tapping Face ID button")
        self.tap(self.FACE_ID_BUTTON)

    def simulate_face_id_success(self):
        log.info("   Simulating Face ID success")
        self.driver.execute_script(
            "mobile: sendBiometricMatch",
            {"type": "faceId", "match": True}
        )

    def simulate_face_id_failure(self):
        log.info("   Simulating Face ID failure")
        self.driver.execute_script(
            "mobile: sendBiometricMatch",
            {"type": "faceId", "match": False}
        )

    # ── Android biometric ─────────────────────────────────────────────────────

    def tap_fingerprint_button(self):
        log.info("   Tapping fingerprint button")
        self.tap(self.FINGERPRINT_BUTTON)

    def simulate_fingerprint_success(self):
        log.info("   Simulating fingerprint success")
        self.driver.finger_print(1)

    def simulate_fingerprint_failure(self):
        log.info("   Simulating fingerprint failure")
        self.driver.finger_print(0)

    # ── Assertions ────────────────────────────────────────────────────────────

    def is_error_message_visible(self) -> bool:
        result = self.is_visible(self.ERROR_MESSAGE)
        log.info(f"   Error message visible → {result}")
        return result

    def get_error_message_text(self) -> str:
        text = self.get_text(self.ERROR_MESSAGE)
        log.info(f"   Error message text → {text}")
        return text

    def is_forgot_password_screen_visible(self) -> bool:
        return self.is_visible(self.FORGOT_PASSWORD_SCREEN)

    def is_reset_email_confirmation_visible(self) -> bool:
        return self.is_visible(self.RESET_CONFIRMATION)

    # ── Convenience ───────────────────────────────────────────────────────────

    def login(self, email: str, password: str):
        """Full login flow — used by logged_in_driver fixture in conftest."""
        log.info(f"🔐 Logging in as {email}")
        self.wait_for_login_screen()
        self.enter_email(email)
        self.enter_password(password)
        self.tap_login()

    def logout(self):
        """Called during teardown of logged_in_driver fixture."""
        log.info("🔓 Logging out...")
        self.driver.back()