from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

from src.settings import Settings, get_settings


async def init_db(settings: Annotated[Settings, Depends(get_settings)]) -> None:
    engine = create_engine(
        f"mysql+pymysql://{settings.database_user}:{settings.database_password}@{settings.database_domain}/{settings.data_database_name}",
        echo=False,
    )
    SQLModel.metadata.create_all(engine)


class DatabaseEngine:
    def __init__(self, settings: Settings):
        self.engine = create_engine(
            f"mysql+pymysql://{settings.database_user}:{settings.database_password}@{settings.database_domain}/{settings.data_database_name}",
            pool_size=20,
            max_overflow=10,
            echo=False,
            pool_recycle=3600,
        )
        self.session_factory = sessionmaker(self.engine, expire_on_commit=False)
