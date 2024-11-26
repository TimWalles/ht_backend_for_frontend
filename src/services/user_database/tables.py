import uuid
from typing import Optional

from sqlalchemy.orm import registry
from sqlmodel import Field, SQLModel

from src.enums.Roles import Roles


class UserBase(SQLModel, registry=registry()):
    username: str = Field(index=True, unique=True)


class User(UserBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    role: Roles = Field(default=Roles.User.value)
    hashed_password: str = Field()
    deactivated: bool = Field(default=False)


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str
    deactivated: bool


class UserRead(UserBase):
    id: uuid.UUID
    username: str


class UserUpdate(UserBase):
    username: str
    role: Roles
    deactivated: bool
    new_password: str
