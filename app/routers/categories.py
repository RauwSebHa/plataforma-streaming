from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.comment_model import Comment
from app.schemas.comment_schema import CommentCreate

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.post("/")
def create_comment(
    comment: CommentCreate,
    session: Session = Depends(get_session)
):

    new_comment = Comment(
        content=comment.content,
        user_id=comment.user_id,
        video_id=comment.video_id
    )

    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)

    return new_comment


@router.get("/video/{video_id}")
def get_comments_by_video(
    video_id: int,
    session: Session = Depends(get_session)
):

    comments = session.exec(
        select(Comment)
        .where(Comment.video_id == video_id)
    ).all()

    return comments


@router.delete("/{comment_id}")
def delete_comment(
    comment_id: int,
    session: Session = Depends(get_session)
):

    comment = session.get(Comment, comment_id)

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comentario no encontrado"
        )

    session.delete(comment)
    session.commit()

    return {
        "message": "Comentario eliminado"
    }