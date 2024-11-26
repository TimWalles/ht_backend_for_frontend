import uuid
from typing import Annotated, List, Union

from fastapi import APIRouter, Depends, HTTPException

from src.operations.auth import get_current_active_user
from src.services.user_database.tables import User

router = APIRouter(prefix="/data", tags=["data"])


# region get routes
@router.get("/get", response_model=List[dict], status_code=200, summary="Get data")
async def get_data(
    user: Annotated[User, Depends(get_current_active_user)],
) -> List[dict]:
    return [{"id": uuid.uuid4(), "name": "Data"}]
