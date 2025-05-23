import allure
from selene import browser, be, have

from data.enums import CourseOptionsCheckbox
from stepik.ui.utils import page_is_loaded


class CatalogPage:

    @allure.step("Открытие Каталога курсов")
    def open(self):
        browser.open('/catalog')
        browser.wait.until(page_is_loaded)

    @allure.step("Ввод названия курса в поле поиска")
    def fill_course_name(self, course_name):
        browser.element('.search-form__input').type(course_name)
        return self

    @allure.step("Нажатие на кнопку поиска")
    def submit_search_button(self):
        browser.element('.search-form__submit').should(be.clickable).click()
        return self

    @staticmethod
    def select_course_option(value: str):
        browser.element('.search-form__form').all('.form-checkbox').element_by(have.exact_text(value)).should(be.clickable).click()

    @allure.step("Выбрать только бесплатные курсы")
    def click_free_checkbox(self):
        self.select_course_option(CourseOptionsCheckbox.FREE.value)
        return self

    @allure.step("Выбрать только курсы с сертификатом")
    def click_certificate_checkbox(self):
        self.select_course_option(CourseOptionsCheckbox.CERTIFICATE.value)
        return self

