import allure
import pytest

from data import fake
from data.data import UserData
from stepik.api.models.enroll import Enrollments
from stepik.api.models.token import Token
from tests.api.conftest import api_client


class TestApi:

    @allure.title('Успешная авторизация через OAuth 2.0 для зарегистрированного пользователя')
    def test_successful_authorization_with_oauth2_by_registered_user(self, api_client):
        response = api_client.oauth2_request()
        assert response.status_code == 200
        Token.model_validate(response.json())

    @allure.title('Авторизация через OAuth 2.0 с некорректными учетными данными')
    @pytest.mark.parametrize(
        "client_id, client_secret",
        [
            (fake.invalid_client_id, UserData.CLIENT_SECRET),
            (UserData.CLIENT_ID, fake.invalid_client_secret),
            (fake.invalid_client_id, fake.invalid_client_secret),
        ],
        ids = [
            "Invalid client_id",
            "Invalid client_secret",
            "Invalid client_id and client_secret"
        ]
    )
    def test_unsuccessful_authorization_invalid_credentials(self, api_client, client_id, client_secret):
        response = api_client.oauth2_request(client_id = client_id, client_secret = client_secret)
        assert response.status_code == 401
        assert response.json().get("error") == "invalid_client"

    @allure.title("Успешная запись на курс")
    def test_enroll_to_course(self, api_client):
        response = api_client.enroll_to_course(course_id = 63085)
        assert response.status_code == 201
        Enrollments.model_validate(response.json())

    @allure.title("Покинуть курс")
    def test_drop_out_course(self, api_client):
        response = api_client.drop_out_course(course_id = 63085)
        assert response.status_code == 204
