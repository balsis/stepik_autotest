from selene import browser as android_app, have

from helpers.mobile.custom_locator import by_id


class ProfilePage:

    def validate_user_name(self):
        android_app.element(by_id("profileName")).should(have.text("John Doe"))
        return self
