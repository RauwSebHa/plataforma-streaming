from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from passlib.context import CryptContext

from app.database import get_session
from app.models.user_model import User
from app.schemas.user_schema import (
    UserRegister,
    UserLogin
)

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
            detail="El correo ya existe"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {
        "message": "Usuario registrado correctamente",
        "user_id": new_user.id
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
        "message": "Login exitoso",
        "user_id": user.id,
        "username": user.username
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

    return user