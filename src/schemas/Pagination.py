from typing import Any, List, Optional

from pydantic import BaseModel


class PaginationBase(BaseModel):
    page: int
    page_size: int
    total: Optional[int]


class PaginationResponse(BaseModel):
    page: int
    page_size: int
    total: int
