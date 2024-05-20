from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MaxLen, MinLen


class User(BaseModel):
    id: Annotated[str, MinLen(4), MaxLen(20)]
    email: EmailStr
    username: str
    password: str
    role: str
