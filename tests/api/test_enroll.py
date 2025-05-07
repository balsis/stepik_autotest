import allure

from stepik.api.models.enroll import Enrollments
from stepik.api.models.user_courses import UserCourses


class TestEnroll:
    @allure.title("Проверка, что юзер нигде не обучается")
    def test_user_courses(self, api_client, drop_out):
        response = api_client.get_user_courses()
        assert response.status_code == 200
        user_courses = UserCourses.model_validate(response.json())
        assert user_courses.user_courses == []

    @allure.title("Получение активных курсов пользователя")
    def test_user_courses(self, api_client, enroll_and_drop_out):
        course_id = enroll_and_drop_out
        response = api_client.get_user_courses()
        assert response.status_code == 200
        user_courses = UserCourses.model_validate(response.json())
        assert user_courses.user_courses[0].course == course_id

    @allure.title("Успешная запись на курс")
    def test_enroll_to_course(self, api_client, drop_out):
        response = api_client.enroll_to_course(course_id = 63085)
        assert response.status_code == 201
        Enrollments.model_validate(response.json())

    @allure.title("Покинуть курс")
    def test_drop_out_course(self, api_client, enroll_user_on_course):
        response = api_client.drop_out_course(course_id = 63085)
        assert response.status_code == 204
