import pytest

from stepik.api.api_client import ApiClient


@pytest.fixture(scope = "session")
def api_client():
    return ApiClient()


@pytest.fixture
def start_and_leave_courses(api_client, request):
    course_id = request.param
    api_client.start_course(course_id)
    yield course_id
    api_client.leave_course(course_id)


@pytest.fixture
def clear_user_courses(api_client):
    yield api_client
    response = api_client.get_user_courses()
    user_courses = response.json().get("user-courses", [])
    for course in user_courses:
        api_client.leave_course(course_id = course["course"])
