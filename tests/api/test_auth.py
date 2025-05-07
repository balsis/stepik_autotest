import allure

from data import fake


class TestApi:

    @allure.title('Authorization succeeded with OAuth 2.0 by registered user')
    def test_successful_authorization_with_oauth2_by_registered_user(self, api_client):
        response = api_client.oauth2_request()
        assert response.status_code == 200
        api_client.validate_oauth2_response(response.json())

    @allure.title('Authorization with OAuth 2.0 with incorrect password')
    def test_unsuccessful_authorization_with_incorrect_password(self, api_client):
        response = api_client.oauth2_request(client_secret = fake.invalid_secret)
        assert response.status_code == 401
        assert response.json().get("error") == "invalid_client"

    def test_get_user_wish_list(self):
        pass
