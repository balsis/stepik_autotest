import requests
from requests import Session
from requests.auth import HTTPBasicAuth

from config import project_config
from data.data import UserData
from helpers.logger import http_logger
from stepik.api.models.token import Token


class Endpoints:
    def __init__(self):
        self.base_url = project_config.base.base_url

    def _get_request_url(self, path):
        return self.base_url + path

    def get_access_token(self):
        return self._get_request_url('/oauth2/token/')

    def get_course_list(self, course_list_number):
        return self._get_request_url(f'/api/course-lists/{course_list_number}')

    def get_course_name(self, course_id):
        return self._get_request_url(f'/api/courses/{course_id}')

    def get_profile_info(self, profile_id):
        return self._get_request_url(f'/api/users/{profile_id}')

    def update_profile_info(self, profile_id):
        return self._get_request_url(f'/api/profiles/{profile_id}')

    def get_user_wishlist(self):
        return self._get_request_url('/api/wish-lists/')

    def delete_course_from_wishlist(self, wishlist_item_id):
        return self._get_request_url(f'/api/wish-lists/{wishlist_item_id}')

    def get_user_enrollments(self):
        return self._get_request_url('/api/enrollments')

    def delete_course_from_enrollments(self, enrollment_id):
        return self._get_request_url(f'/api/enrollments/{enrollment_id}')


class ApiClient:
    def __init__(self):
        self.endpoints = Endpoints()
        self.session = Session()
        self.token = self.get_access_token()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def oauth2_request(self, client_id=UserData.CLIENT_ID, client_secret=UserData.CLIENT_SECRET) -> requests.Response:
        auth = HTTPBasicAuth(client_id, client_secret)
        response = self.session.post(self.endpoints.get_access_token(),
                                     data = {'grant_type': 'client_credentials'},
                                     auth = auth)
        return response

    def get_access_token(self):
        return self.oauth2_request().json().get('access_token')

    @staticmethod
    def validate_oauth2_response(response):
        return Token(**response)

    @http_logger()
    def get_course_list(self, course_list_number: int):
        return self.session.get(self.endpoints.get_course_list(course_list_number))

    @http_logger()
    def get_course_name(self, course_id: int) -> str:
        response = self.session.get(self.endpoints.get_course_name(course_id))
        return response.json()['courses'][0]['title']

    @http_logger()
    def get_profile_info(self, profile_id: int):
        return self.session.get(self.endpoints.get_profile_info(profile_id))

    @http_logger()
    def update_profile_info(self, profile_id: int, data: dict):
        return self.session.put(self.endpoints.update_profile_info(profile_id), json = data)

    @http_logger()
    def get_user_wish_list(self):
        response = self.session.get(self.endpoints.get_user_wishlist())
        return response.json()['wish-lists']

    @http_logger()
    def delete_course_from_wishlist(self, course_id: int):
        wish_list = self.get_user_wish_list()
        for item in wish_list:
            if item['course'] == course_id:
                wishlist_item_id = item['id']
                return self.session.delete(self.endpoints.delete_course_from_wishlist(wishlist_item_id))
        raise ValueError(f"Course ID {course_id} not found in wishlist")

    @http_logger()
    def get_user_enrollments(self):
        return self.session.get(self.endpoints.get_user_enrollments())

    @http_logger()
    def delete_course_from_enrollments(self, course_id: int):
        enrollments = self.get_user_enrollments().json()['enrollments']
        for enrollment in enrollments:
            if enrollment['course'] == course_id:
                enrollment_id = enrollment['id']
                return self.session.delete(self.endpoints.delete_course_from_enrollments(enrollment_id))
        raise ValueError(f"Course ID {course_id} not found in enrollments")
