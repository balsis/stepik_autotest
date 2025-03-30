import allure

from data import fake
from model import app


@allure.parent_suite("Поиск")
@allure.suite("Поиск из навигационной панели")
@allure.epic("Поиск")
@allure.feature("Поиск из навигационной панели")
class TestNavbarSearch:

    @allure.sub_suite("Поиск курса по названию")
    @allure.story("Поиск курса по названию")
    @allure.title("Поиск курса с валидным названием из навигационной панели")
    def test_search_course_with_valid_keyword_from_navbar(self):
        app.catalog_page.open()
        app.navbar.find_course(course_name = "Инди-курс программирования на Python")
        app.catalog_search_page.should_have_course_with_title(title = "Инди-курс программирования на Python")

    @allure.sub_suite("Поиск курса по названию")
    @allure.story("Поиск курса по названию")
    @allure.title("Поиск курса с невалидным названием из навигационной панели")
    def test_search_course_with_invalid_keyword_from_navbar(self):
        app.catalog_page.open()
        app.navbar.find_course(course_name = fake.random_invalid_search_keyword)
        app.catalog_search_page.should_have_nothing_found_message(value = fake.random_invalid_search_keyword)


@allure.parent_suite("Поиск")
@allure.suite("Поиск в Каталоге")
@allure.epic("Поиск")
@allure.feature("Поиск в Каталоге")
class TestCatalogSearch:

    @allure.sub_suite("Поиск курса по названию")
    @allure.story("Поиск курса по названию")
    @allure.title("Поиск курса с валидным названием в Каталоге")
    def test_search_course_with_valid_keyword_from_catalog(self):
        app.catalog_page.open()
        app.catalog_page.fill_course_name(course_name = "Инди-курс программирования на Python")
        app.catalog_page.submit_search_button()
        app.catalog_search_page.should_have_course_with_title(title = "Инди-курс программирования на Python")

    @allure.sub_suite("Поиск курсов по фильтрам")
    @allure.story("Поиск курсов по фильтрам")
    @allure.title("Поиск в Каталоге бесплатных курсов")
    def test_search_free_courses(self):
        app.catalog_page.open()
        app.catalog_page.click_free_checkbox()
        app.catalog_page.submit_search_button()
        app.catalog_search_page.all_courses_should_have_free_prices()

    @allure.sub_suite("Поиск курсов по фильтрам")
    @allure.story("Поиск курсов по фильтрам")
    @allure.title("Поиск в Каталоге курсов с сертификатами")
    def test_search_courses_with_certs(self):
        app.catalog_page.open()
        app.catalog_page.click_certificate_checkbox()
        app.catalog_page.submit_search_button()
        app.catalog_search_page.all_courses_should_have_certificate()

    @allure.sub_suite("Поиск курса по названию")
    @allure.story("Поиск курса по названию")
    @allure.title("Поиск курса с невалидным названием в Каталоге")
    def test_search_course_with_invalid_keyword_from_catalog(self):
        app.catalog_page.open()
        app.catalog_page.fill_course_name(course_name = fake.random_invalid_search_keyword)
        app.catalog_page.submit_search_button()
        app.catalog_search_page.should_have_nothing_found_message(value = fake.random_invalid_search_keyword)
