from typing import List

from pydantic import BaseModel, Field

from stepik.api.models.meta import Meta


class UserCourse(BaseModel):
    id: int
    user: int
    course: int
    is_favorite: bool
    is_pinned: bool
    is_archived: bool
    last_viewed: str
    can_be_reviewed: bool


class UserCourses(BaseModel):
    meta: Meta
    user_courses: List[UserCourse] = Field(..., alias = 'user-courses')
