import pytest

from stepik.api.client import ApiClient


@pytest.fixture(scope = "session")
def api_client():
    return ApiClient()


@pytest.fixture
def enroll_user_on_course(api_client):
    course_id = 63085
    api_client.enroll_to_course(course_id)
    yield course_id


@pytest.fixture
def enroll_and_drop_out(api_client):
    course_id = 63085
    api_client.enroll_to_course(course_id)
    yield course_id
    api_client.drop_out_course(course_id)


@pytest.fixture
def drop_out(api_client):
    course_id = 63085
    yield api_client
    api_client.drop_out_course(course_id)
