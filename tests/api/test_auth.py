import allure
import pytest

from data import fake
from data.credentials_data import UserData
from stepik.api.models.token import Token
from tests.api.conftest import api_client


@allure.parent_suite("API")
@allure.suite("API авторизация через OAuth 2.0")
@allure.epic("API")
@allure.feature("API авторизация через OAuth 2.0")
class TestAuthApi:

    @allure.sub_suite("Авторизация с валидными данными")
    @allure.story("Авторизация с валидными данными")
    @allure.title('Успешная авторизация через OAuth 2.0 для зарегистрированного пользователя')
    def test_successful_authorization_with_oauth2_by_registered_user(self, api_client):
        response = api_client.oauth2_request()
        assert response.status_code == 200
        Token.model_validate(response.json())

    @allure.sub_suite("Авторизация с невалидными данными")
    @allure.story("Авторизация с невалидными данными")
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
