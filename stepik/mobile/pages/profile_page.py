from selene import browser as android_app, have


class ProfilePage:

    def validate_user_name(self):
        android_app.element(("id", "org.stepic.droid:id/profileName")).should(have.text("John Doe"))
        return self
