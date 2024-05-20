from posts.schemas import Post


def create_post(post: Post) -> dict:
    return {
        "success": True,
        "post": post,
    }
