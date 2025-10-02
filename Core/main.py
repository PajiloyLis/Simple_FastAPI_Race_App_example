import os

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from Core.Config.Settings import Settings
from Database.Database import Database
from HttpServer.Controller.RaceController import RaceController
from Database.Repository.RacePostgresRepository import RaceRepository
from Service.RaceService import RaceService
from Database.Models.DriverPostgresDB import DriverPostgresDB
from Database.Models.RacePostgresDB import RacePostgresDB
from Database.Models.TrackPostgresDB import TrackPostgresDB
from Database.Models.ParticipationPostgresDB import ParticipationPostgresDB
from Database.Models.TeamPostgresDB import TeamPostgresDB
from Database.Models.SeasonPostgresDB import SeasonPostgresDB


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    database = Database()

    await database.connect(db_url=settings.database_url)
    
    # Create tables
    from Database.Models.BaseModel import BaseModel
    async with database.get_session() as session:
        async with session.bind.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
    
    controllers = await create_controllers(app)

    await register_routers(app, controllers)

    yield

    await database.disconnect()


async def create_controllers(app: FastAPI):
    # Create dependencies manually
    database = Database()
    session = database.get_session()
    race_repository = RaceRepository(session)
    race_service = RaceService(race_repository)
    race_controller = RaceController(race_service)
    return [race_controller]

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
    uvicorn.run("Core.main:app", host=settings.host, port=settings.port, log_level="info", reload=True)