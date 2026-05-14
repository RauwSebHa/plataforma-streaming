from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

from app.routers import users
from app.routers import videos
from app.routers import comments
from app.routers import categories
from app.models.user_model import User
from app.models.video_model import Video
from app.models.comment_model import Comment
from app.models.category_model import Category

app = FastAPI(title="StreamCloud API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(videos.router)
app.include_router(comments.router)
app.include_router(categories.router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

from app.routers import users
from app.routers import videos
from app.routers import comments
from app.routers import categories

from app.models.user_model import User
from app.models.video_model import Video
from app.models.comment_model import Comment
from app.models.category_model import Category


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(videos.router)
app.include_router(comments.router)
app.include_router(categories.router)


@app.get("/")
def root():
    return {"message": "Streaming Platform API"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

from app.routers import users
from app.routers import videos
from app.routers import comments
from app.routers import categories

from app.models.user_model import User
from app.models.video_model import Video
from app.models.comment_model import Comment
from app.models.category_model import Category


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(videos.router)
app.include_router(comments.router)
app.include_router(categories.router)


@app.get("/")
def root():
    return {
        "message": "Streaming Platform API"
    }
