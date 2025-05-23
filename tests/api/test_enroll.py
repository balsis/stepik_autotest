import allure
import pytest

from stepik.api.models.enroll import Enrollments
from stepik.api.models.user_courses import UserCourses


@allure.parent_suite("API")
@allure.suite("Активные курсы пользователя")
class TestEnroll:

    @allure.sub_suite("Текущие активные курсы пользователя")
    @allure.title("Пользователь не присоединился ни к одному курсу")
    def test_user_has_no_courses(self, api_client, clear_user_courses):
        response = api_client.get_user_courses()
        assert response.status_code == 200
        user_courses = UserCourses.model_validate(response.json())
        assert user_courses.user_courses == []

    @allure.sub_suite("Поступление на курс")
    @allure.title("Успешная запись на курс")
    @pytest.mark.parametrize('start_and_leave_courses', [63085], indirect = True)
    def test_enroll_to_course(self, api_client, start_and_leave_courses):
        course_id = start_and_leave_courses
        response = api_client.start_course(course_id)
        assert response.status_code == 201
        Enrollments.model_validate(response.json())

    @allure.sub_suite("Текущие активные курсы пользователя")
    @allure.title("Получение активных курсов пользователя")
    @pytest.mark.parametrize('start_and_leave_courses', [63085], indirect = True)
    def test_user_courses_after_enroll(self, api_client, start_and_leave_courses):
        course_id = start_and_leave_courses
        response = api_client.get_user_courses()
        assert response.status_code == 200
        user_courses = UserCourses.model_validate(response.json())
        assert any(uc.course == course_id for uc in user_courses.user_courses)

    @allure.sub_suite("Поступление на курс")
    @allure.title("Успешная запись на несколько курсов")
    def test_enroll_to_multiple_courses(self, api_client, clear_user_courses):
        course_ids_to_enroll = [63085, 58852]

        for course_id in course_ids_to_enroll:
            enroll_response = api_client.start_course(course_id = course_id)
            assert enroll_response.status_code == 201
            Enrollments.model_validate(enroll_response.json())
        user_courses_response = api_client.get_user_courses().json()
        user_courses_model = UserCourses.model_validate(user_courses_response)
        assert len(user_courses_model.user_courses) == 2
        enrolled_course_ids = [uc.course for uc in user_courses_model.user_courses]
        assert sorted(enrolled_course_ids) == sorted(course_ids_to_enroll)

    @allure.sub_suite("Окончание учебы на курсе")
    @allure.title("Покинуть курс")
    @pytest.mark.parametrize('start_and_leave_courses', [63085], indirect = True)
    def test_drop_out_course(self, api_client, start_and_leave_courses):
        course_id = start_and_leave_courses
        response = api_client.leave_course(course_id)
        assert response.status_code == 204
