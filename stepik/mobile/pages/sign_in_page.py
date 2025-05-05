from selene import browser as android_app, have, be

from helpers.mobile.custom_locator import by_id


class SignInPage:
    def skip_authorisation(self):
        android_app.element(by_id('dismissButton')).should(be.clickable).click()
        return self

    def tap_sign_in_with_email_button(self):
        android_app.element(by_id('signInWithEmail')).click()
        return self

    def fill_email_and_password(self, email: str, password: str):
        android_app.element(by_id('loginField')).type(email)
        android_app.element(by_id('passwordField')).type(password)
        return self

    def tap_login_button(self):
        android_app.element(by_id('loginButton')).click()
        return self

    def validate_greeting_panel(self):
        android_app.element(by_id('headerTitle')).should(have.text("Greetings!"))
        (android_app.element(("id", "android:id/message")).
         should(have.text("App will help complete course and get certificate. Enable everyday notifications for continuous learning!")))
        return self

    def skip_greeting_panel(self):
        android_app.element(("id", "android:id/button2")).click()
        return self

    def check_login_error_message(self):
        android_app.element(by_id('loginErrorMessage')).should(have.text('Login/password was incorrect'))
        return self
