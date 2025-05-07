import requests


class AuthHelper:
    def __init__(self, base_url="https://stepik.org"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_csrftoken(self):
        self.session.get(f"{self.base_url}", verify = False)
        csrftoken = self.session.cookies.get('csrftoken')
        return csrftoken

    def login(self, email, password):
        csrftoken = self.get_csrftoken()
        self.session.headers.update({
            "X-CSRFToken": csrftoken,
            "Origin": self.base_url,
            "Referer": f"{self.base_url}",
        })
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(
            f"{self.base_url}/api/users/login",
            json = payload,
            verify = False
        )
        if response.status_code == 204:
            return {
                'csrftoken': self.session.cookies.get('csrftoken'),
                'sessionid': self.session.cookies.get('sessionid')
            }
        else:
            raise Exception(f"Login failed with status code: {response.status_code}")
