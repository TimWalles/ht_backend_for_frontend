from typing import List, Union

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from src.enums.Tables import Tables
from src.services.data_database.tables import (
    Activity,
    ActivityCreate,
    Reward,
    RewardCreate,
)
from src.utils import uuid_to_str


# region add data
async def add_data(
    session: Session,
    data: Union[RewardCreate, ActivityCreate],
    user_id: str | None = None,
) -> Union[Reward]:
    try:
        match data:
            case RewardCreate():
                db_data = Reward.model_validate(data)
            case ActivityCreate():
                data = data.model_dump()
                data["user_id"] = user_id
                db_data = Activity.model_validate(data)
            case _:
                raise ValueError("Invalid data type")
        session.add(db_data)
        session.commit()
        session.refresh(db_data)
        return db_data
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Data already exists: {str(e)}",
        )
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to add data: {str(e)}",
        )


# endregion


# region get data
async def get_data(
    session: Session,
    table: Tables,
) -> List[Union[Reward, Activity]]:
    try:
        match table:
            case Tables.Rewards:
                statement = select(Reward)
            case Tables.Activity:
                statement = select(Activity)
            case _:
                raise ValueError("Invalid table type")
        return session.exec(statement).fetchall()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to get data: {str(e)}",
        )


async def get_data_with_relationship(
    session: Session,
    table: Tables,
) -> List[Union[Reward, Activity]]:
    try:
        match table:
            case Tables.Rewards:
                statement = select(Reward)
            case Tables.Activity:
                statement = select(Activity)
            case _:
                raise ValueError("Invalid table type")
        return session.exec(statement).fetchall()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to get data: {str(e)}",
        )


# endregion
