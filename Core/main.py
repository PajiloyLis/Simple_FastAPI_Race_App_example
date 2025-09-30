import os

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from Core.Config.Settings import Settings
from Database.Database import Database
from HttpServer.Controller.RaceController import RaceController
from HttpServer.ControllerDependencyInjector import get_race_controller


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    database = Database()

    await database.connect(db_url=settings.database_url)
    controllers = await create_controllers(app)

    await register_routers(app, controllers)

    yield

    await database.disconnect()


async def create_controllers(app: FastAPI):
    return [await get_race_controller()]

async def register_routers(app: FastAPI, controllers) -> None:
    for controller in controllers:
        app.include_router(controller.router)


app = FastAPI(
    title="Racing",
    description="Simple Fast API",
    version="1.0",
    lifespan=lifespan
)

if __name__ == "__main__":
    settings = Settings()
    uvicorn.run("main:app", host=settings.host, port=settings.port, log_level="info", reload=True)