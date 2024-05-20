from fastapi import APIRouter
from posts import crud
from posts.schemas import Post

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post('/create')
def add_post(post: Post):
    return crud.create_post(post)
