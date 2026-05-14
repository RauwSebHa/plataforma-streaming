from pydantic import BaseModel
from typing import Optional


class VideoCreate(BaseModel):
    title: str
    description: Optional[str]
    video_url: str
    thumbnail_url: Optional[str]
    user_id: int
    category_id: int