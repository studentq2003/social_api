from fastapi import APIRouter

from users import crud
from users.schemas import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: User):
    return crud.create_user(user)
