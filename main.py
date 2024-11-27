from fastapi import FastAPI

from src.routers import auth, data, user
from src.services.data_database.engine import init_db
from src.services.user_database.engine import init_user_db
from src.settings import get_settings


async def lifespan(app: FastAPI):
    await init_user_db(settings=get_settings())
    await init_db(settings=get_settings())
    yield


# region app
app = FastAPI(lifespan=lifespan)


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(data.router)
