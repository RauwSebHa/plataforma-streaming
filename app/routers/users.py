from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from passlib.context import CryptContext

from app.database import get_session
from app.models.user_model import User
from app.models.video_model import Video
from app.schemas.user_schema import UserRegister, UserLogin


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


@router.post("/register")
def register_user(
    user: UserRegister,
    session: Session = Depends(get_session)
):
    existing_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="El correo ya está registrado"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        profile_image_url=user.profile_image_url
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {
        "message": "Usuario registrado correctamente",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "profile_image_url": new_user.profile_image_url
        }
    }


@router.post("/login")
def login_user(
    credentials: UserLogin,
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.email == credentials.email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    if not pwd_context.verify(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Contraseña incorrecta"
        )

    return {
        "message": "Inicio de sesión exitoso",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profile_image_url": user.profile_image_url
        }
    }


@router.get("/{user_id}")
def get_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "profile_image_url": user.profile_image_url,
        "created_at": user.created_at
    }


@router.get("/{user_id}/videos")
def get_user_videos(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    videos = session.exec(
        select(Video).where(Video.user_id == user_id)
    ).all()

    return videos