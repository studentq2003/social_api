from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel


class Post(BaseModel):
    author_id: int
    text: Annotated[str, MaxLen(5000)]
    date: str
    access: str
    likes: Annotated[list, None]
