import pytest

from stepik.api.client import ApiClient


@pytest.fixture(scope = "session")
def api_client():
    return ApiClient()


@pytest.fixture
def enroll_and_drop_out(api_client, request):
    course_id = request.param
    api_client.enroll_to_course(course_id)
    yield course_id
    api_client.drop_out_course(course_id)


@pytest.fixture
def enroll_and_drop_out(api_client, request):
    course_id = request.param
    api_client.enroll_to_course(course_id)
    yield course_id
    api_client.drop_out_course(course_id)


@pytest.fixture
def clear_user_courses_after(api_client):
    yield api_client
    response = api_client.get_user_courses()
    user_courses = response.json().get("user-courses", [])
    for course in user_courses:
        api_client.drop_out_course(course_id = course["course"])
