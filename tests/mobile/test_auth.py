from data import fake
from data.data import UserData
from stepik.mobile import android_app


def test_login_with_email_and_password(android_management):
    android_app.onboarding_page.skip_onboarding()
    android_app.sign_in_page.tap_sign_in_with_email_button()
    android_app.sign_in_page.fill_email_and_password(email = UserData.STEPIK_EMAIL, password = UserData.STEPIK_PASSWORD)
    android_app.sign_in_page.tap_login_button()
    android_app.sign_in_page.validate_greeting_panel().skip_greeting_panel()
    android_app.navbar.select_profile_view()
    android_app.profile_page.validate_user_name()


def test_login_with_invalid_email_password(android_management):
    android_app.onboarding_page.skip_onboarding()
    android_app.sign_in_page.tap_sign_in_with_email_button()
    android_app.sign_in_page.fill_email_and_password(email = fake.wrong_email, password = fake.wrong_password)
    android_app.sign_in_page.tap_login_button()
    android_app.sign_in_page.check_login_error_message()
