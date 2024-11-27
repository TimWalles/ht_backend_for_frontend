from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import exc
from sqlmodel import Session

from src.dependencies import get_user_db_session
from src.operations.user import create_new_user, get_users
from src.services.user_database.tables import UserCreate, UserRead

router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/create/",
    response_model=UserRead,
    summary="Create a new user",
)
async def create_user(
    user: UserCreate,
    session: Session = Depends(get_user_db_session),
):
    try:
        return await create_new_user(
            session=session,
            user=user,
        )
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exists",
        )


@router.get(
    "/all/",
    response_model=List[UserRead],
    summary="Get a user all users",
)
async def get_user(
    session: Session = Depends(get_user_db_session),
):
    try:
        return await get_users(
            session=session,
        )
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exists",
        )
