from pydantic import BaseModel


class CommentCreate(BaseModel):
    content: str
    user_id: int
    video_id: int