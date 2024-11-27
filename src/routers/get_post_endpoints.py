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

#Retrieve all employees (employee_table)
@router.get(
    "/employee_table/all",
    response_model=List[EmployeeRead],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all employees",
)
async def get_all_employees(
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Retrieve all employees from the 'employee_table'.
    """
    try:
        return await get_data(session=session, table="employee_table")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

# Add a new employee (employee_table)
@router.post(
    "/employee_table/add",
    response_model=EmployeeRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new employee",
)
async def create_employee(
    employee: EmployeeCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Add a new employee to the 'employee_table'.
    """
    try:
        return await add_data(session=session, data=employee)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



# Retrieve all activities (activity_table)

@router.get(
    "/activity_table/all",
    response_model=List[ActivityRead],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all activities",
)
async def get_all_activities(
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Retrieve all activities from the 'activity_table'.
    """
    try:
        return await get_data(session=session, table="activity_table")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Add a new activity (activity_table)

@router.post(
    "/activity_table/add",
    response_model=ActivityRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new activity",
)
async def create_activity(
    activity: ActivityCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Add a new activity to the 'activity_table'.
    """
    try:
        return await add_data(session=session, data=activity)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Retrieve all rewards (reward_table)

@router.get(
    "/reward_table/all",
    response_model=List[RewardRead],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all rewards",
)
async def get_all_rewards(
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Retrieve all rewards from the 'reward_table'.
    """
    try:
        return await get_data(session=session, table="reward_table")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
#Add a new reward (reward_table)

@router.post(
    "/reward_table/add",
    response_model=RewardRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new reward",
)
async def create_reward(
    reward: RewardCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Add a new reward to the 'reward_table'.
    """
    try:
        return await add_data(session=session, data=reward)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Retrieve all tracking records (tracking_table)

@router.get(
    "/tracking_table/all",
    response_model=List[TrackingRead],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all tracking records",
)
async def get_all_tracking(
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Retrieve all records from the 'tracking_table'.
    """
    try:
        return await get_data(session=session, table="tracking_table")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Add a new tracking record (tracking_table)

@router.post(
    "/tracking_table/add",
    response_model=TrackingRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new tracking record",
)
async def create_tracking(
    tracking: TrackingCreate,
    session: Session = Depends(get_data_db_session),
    current_user: User = Depends(get_current_active_user),
):
    """
    Add a new record to the 'tracking_table'.
    """
    try:
        return await add_data(session=session, data=tracking)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))