import allure
import requests
from requests import Session
from requests.auth import HTTPBasicAuth

from config import project_config
from data.credentials_data import UserData
from helpers.logger import http_logger


class Endpoints:
    ACCESS_TOKEN = "/oauth2/token/"
    USER_COURSES = "/api/user-courses"
    ENROLLMENTS = "/api/enrollments"

    @staticmethod
    def delete_enrollment(course_id: str) -> str:
        return f"/api/enrollments/{course_id}"


class ApiClient:
    def __init__(self):
        self.endpoints = Endpoints()
        self.session = Session()
        self.base_url = project_config.base.base_url
        self.token = self.get_access_token()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def make_url(self, path: str) -> str:
        return self.base_url + path

    @allure.step("Запрос OAuth 2.0 авторизации")
    @http_logger()
    def oauth2_request(self, client_id=UserData.CLIENT_ID, client_secret=UserData.CLIENT_SECRET) -> requests.Response:
        auth = HTTPBasicAuth(client_id, client_secret)
        response = self.session.post(self.make_url(self.endpoints.ACCESS_TOKEN),
                                     data = {'grant_type': 'client_credentials'},
                                     auth = auth,
                                     verify = False)
        return response

    @allure.step("Извлечение access токена из ответа ")
    def get_access_token(self) -> str:
        return self.oauth2_request().json().get('access_token')

    @allure.step("Получение текущих курсов пользователя")
    @http_logger()
    def get_user_courses(self) -> requests.Response:
        return self.session.get(self.make_url(self.endpoints.USER_COURSES), verify = False)

    @allure.step("Начало учебы на курсе")
    @http_logger()
    def start_course(self, course_id: int):
        payload = {
            "enrollment": {
                "course": str(course_id)
            }
        }
        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        return self.session.post(self.make_url(self.endpoints.ENROLLMENTS), json = payload, headers = headers, verify = False)

    @allure.step("Покинуть курс")
    @http_logger()
    def leave_course(self, course_id: int):
        return self.session.delete(self.make_url(self.endpoints.delete_enrollment(str(course_id))), verify = False)
