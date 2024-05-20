from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel


class Post(BaseModel):
    author_id: int
    text: Annotated[str, MaxLen(5000)]
    date: str
    access: str
    access_group: Annotated[list, None] = None
    likes: Annotated[list, None]
