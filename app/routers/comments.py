from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from app.database import get_session
from app.models.video_model import Video
from app.schemas.video_schema import VideoCreate

router = APIRouter(
    prefix="/videos",
    tags=["Videos"]
)


@router.post("/")
def create_video(
    video: VideoCreate,
    session: Session = Depends(get_session)
):

    new_video = Video(
        title=video.title,
        description=video.description,
        video_url=video.video_url,
        thumbnail_url=video.thumbnail_url,
        user_id=video.user_id,
        category_id=video.category_id
    )

    session.add(new_video)
    session.commit()
    session.refresh(new_video)

    return new_video


@router.get("/")
def get_videos(
    session: Session = Depends(get_session)
):

    videos = session.exec(
        select(Video)
    ).all()

    return videos


@router.get("/recent")
def get_recent_videos(
    session: Session = Depends(get_session)
):

    videos = session.exec(
        select(Video)
        .order_by(Video.created_at.desc())
        .limit(10)
    ).all()

    return videos


@router.get("/search")
def search_videos(
    q: str = Query(...),
    session: Session = Depends(get_session)
):

    videos = session.exec(
        select(Video)
        .where(Video.title.contains(q))
    ).all()

    return videos


@router.get("/{video_id}")
def get_video(
    video_id: int,
    session: Session = Depends(get_session)
):

    video = session.get(Video, video_id)

    if not video:
        raise HTTPException(
            status_code=404,
            detail="Video no encontrado"
        )

    return video


@router.delete("/{video_id}")
def delete_video(
    video_id: int,
    session: Session = Depends(get_session)
):

    video = session.get(Video, video_id)

    if not video:
        raise HTTPException(
            status_code=404,
            detail="Video no encontrado"
        )

    session.delete(video)
    session.commit()

    return {
        "message": "Video eliminado correctamente"
    }