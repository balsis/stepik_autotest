import pytest

from stepik.api.client import ApiClient


@pytest.fixture(scope = "session")
def api_client():
    return ApiClient()
