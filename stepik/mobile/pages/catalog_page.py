import allure
from selene import browser as android_app, have

from data.enums import Language
from helpers.mobile.custom_locator import by_id
from helpers.mobile.gestures import Gestures


class CatalogPage(Gestures):
    @allure.step("Выбор языка")
    def select_language(self, language: Language):
        if language == Language.EN:
            android_app.element(by_id('languageEn')).click()
            android_app.element(by_id('languageEn')).should(have.attribute('checked').value('true'))
        elif language == Language.RU:
            android_app.element(by_id('languageRu')).click()
            android_app.element(by_id('languageRu')).should(have.attribute('checked').value('true'))
        return self

    @allure.step("Проверка наличия основных категорий в каталоге")
    def check_main_categories_in_catalog(self, *categories: str, max_swipes: int = 5) -> None:
        for category in categories:
            self.find_text_with_scrolling(text = category, max_swipes = max_swipes)

    @property
    def course_titles(self):
        return android_app.all(by_id('courseItemName')).with_(timeout = 20)

    @allure.step("Проверка наличия курса с наименованием {title} среди найденных")
    def should_have_course_with_title(self, title: str):
        self.course_titles.first.should(have.text(title))

    @allure.step("Ввод названия курса в поле поиска")
    def fill_course_name(self, course_name):
        search_input = android_app.element(by_id('search_src_text')).click()
        search_input.type(course_name)
        android_app.driver.press_keycode(66)
        return self
