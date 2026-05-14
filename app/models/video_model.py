from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Video(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str
    description: Optional[str] = None

    video_url: str
    thumbnail_url: Optional[str] = None

    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")

    created_at: datetime = Field(default_factory=datetime.utcnow)