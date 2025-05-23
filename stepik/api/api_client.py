import allure
import requests
from requests import Session
from requests.auth import HTTPBasicAuth

from config import project_config
from data.credentials_data import UserData
from helpers.logger import http_logger


class Endpoints:
    def __init__(self):
        self.base_url = project_config.base.base_url

    def _get_request_url(self, path):
        return self.base_url + path

    def get_access_token(self):
        return self._get_request_url('/oauth2/token/')

    def user_courses(self):
        return self._get_request_url('/api/user-courses')

    def enrollments(self):
        return self._get_request_url('/api/enrollments')

    def delete_enrollment(self, course_id: str):
        return self._get_request_url(f'/api/enrollments/{course_id}')


class ApiClient:
    def __init__(self):
        self.endpoints = Endpoints()
        self.session = Session()
        self.token = self.get_access_token()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    @allure.step("Запрос OAuth 2.0 авторизации")
    @http_logger()
    def oauth2_request(self, client_id=UserData.CLIENT_ID, client_secret=UserData.CLIENT_SECRET) -> requests.Response:
        auth = HTTPBasicAuth(client_id, client_secret)
        response = self.session.post(self.endpoints.get_access_token(),
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
        return self.session.get(self.endpoints.user_courses(), verify = False)

    @allure.step("Начало учебы на курсе")
    @http_logger()
    def enroll_to_course(self, course_id: int):
        payload = {
            "enrollment": {
                "course": str(course_id)
            }
        }
        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        response = self.session.post(self.endpoints.enrollments(), json = payload, headers = headers, verify = False)
        return response

    @allure.step("Покинуть курс")
    @http_logger()
    def drop_out_course(self, course_id: int):
        response = self.session.delete(self.endpoints.delete_enrollment(course_id = course_id), verify = False)
        return response
