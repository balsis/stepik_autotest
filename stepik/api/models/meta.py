from pydantic import BaseModel


class Meta(BaseModel):
    page: int
    has_next: bool
    has_previous: bool
