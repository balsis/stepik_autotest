import allure
from selene import browser as android_app, be

from helpers.mobile.custom_locator import by_id


class Navbar:
    @allure.step("Выбор вкладки 'Home'")
    def select_home_view(self):
        android_app.element(by_id('home')).click().should(be.selected)
        return self

    @allure.step("Выбор вкладки 'Catalog'")
    def select_catalog_view(self):
        android_app.element(by_id('catalog')).click().should(be.selected)
        return self

    @allure.step("Выбор вкладки 'Profile'")
    def select_profile_view(self):
        android_app.element(by_id('profile')).click().should(be.selected)
        return self

    @allure.step("Выбор вкладки 'Notifications'")
    def select_notifications_view(self):
        raise NotImplemented
