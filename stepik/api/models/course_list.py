from typing import List

from pydantic import BaseModel, Field

from stepik.api.models.meta import Meta


class CourseList(BaseModel):
    id: int
    position: int
    title: str
    description: str
    language: str
    platform: int
    social_image_url: str
    courses: list
    similar_authors: list
    similar_course_lists: list
    similar_specializations: list


class CourseListsResponse(BaseModel):
    meta: Meta
    course_lists: List[CourseList] = Field(..., alias = "course-lists")
