import pytest

from data.enums import Language
from stepik.mobile import android_app


@pytest.mark.parametrize(
    "language, categories",
    [
        (Language.EN, ["Editors' choice", "Top categories", "Popular courses"]),
        (Language.RU, ["Новые курсы", "Популярные курсы", "Рекомендованные курсы"])
    ],
    ids = ['Catalog categories in English', 'Catalog categories in Russian']
)
def test_check_main_categories_in_catalog(android_management, language, categories):
    android_app.onboarding_page.skip_onboarding()
    android_app.sign_in_page.skip_authorisation()
    android_app.navbar.select_catalog_view()
    android_app.catalog_page.select_language(language = language)
    android_app.catalog_page.check_main_categories_in_catalog(*categories, max_swipes = 6)


@pytest.mark.parametrize(
    "language, course_name",
    [
        (Language.EN, "Python. Functional Programming"),
        (Language.RU, "Инди-курс программирования на Python")
    ],
    ids = ['English course name', 'Russian course name']
)
def test_find_course_by_name(android_management, language, course_name):
    android_app.onboarding_page.skip_onboarding()
    android_app.sign_in_page.skip_authorisation()
    android_app.navbar.select_catalog_view()
    android_app.catalog_page.select_language(language = language)
    android_app.catalog_page.fill_course_name(course_name = course_name)
    android_app.catalog_page.should_have_course_with_title(title = course_name)
