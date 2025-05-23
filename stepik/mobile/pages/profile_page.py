import allure
from selene import browser as android_app, have

from stepik.mobile.custom_locator import by_id


class ProfilePage:
    @allure.step("Проверка имени в профиле пользователя при успешной авторизации")
    def validate_user_name(self):
        android_app.element(by_id("profileName")).should(have.text("John Doe"))
        return self
