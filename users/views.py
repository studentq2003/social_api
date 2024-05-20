from fastapi import APIRouter

from users.schemas import User
from users import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: User):
    return crud.create_user(user)
