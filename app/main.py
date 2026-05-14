from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

from app.routers import users
from app.routers import videos
from app.routers import comments
from app.routers import categories

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