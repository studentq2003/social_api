import uvicorn
from fastapi import FastAPI

from posts.views import router as post_router
from users.views import router as user_router

app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
