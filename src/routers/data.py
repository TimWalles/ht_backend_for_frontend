import uuid
from typing import Annotated, List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from src.dependencies import get_data_db_session
from src.enums.Tables import Tables
from src.operations.auth import get_current_active_user
from src.operations.data import add_data, get_data
from src.services.data_database.tables import (
    ActivityCreate,
    ActivityRead,
    ActivityReadWithReward,
    RewardCreate,
    RewardRead,
)
from src.services.user_database.tables import User

router = APIRouter(prefix="/data", tags=["data"])


# region get routes
@router.get(
    "/{table}/all",
    response_model=List[Union[RewardRead, ActivityReadWithReward]],
    status_code=status.HTTP_200_OK,
    summary="Get all rewards",
)
async def get_table_data(
    table: Tables,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    try:
        return await get_data(
            session=session,
            table=table,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# endregion


# region post routes
@router.post(
    "/reward/add",
    response_model=RewardRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new reward",
)
async def create_reward(
    reward: RewardCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    try:
        return await add_data(
            session=session,
            data=reward,
        )
        return {}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/activity/add",
    response_model=ActivityCreate,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new reward",
)
async def create_activity(
    reward: ActivityCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):

    try:
        return await add_data(
            session=session,
            data=reward,
            user_id=current_user.id,
        )
        return {}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# endregion
