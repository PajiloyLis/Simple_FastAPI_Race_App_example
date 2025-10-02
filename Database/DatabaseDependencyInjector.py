from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Core.Repository.IRaceRepository import IRaceRepository
from Core.Repository.ITrackRepository import ITrackRepository
from Database.Database import Database
from Database.Repository.RacePostgresRepository import RaceRepository
from Database.Repository.TrackPostgresRepository import TrackRepository


async def get_db_session() -> AsyncSession:
    database = Database()
    if not database.is_connected:
        raise RuntimeError("Database is not connected")
    session = database.get_session()
    try:
        return session
    finally:
        await session.close()


async def get_race_repository() -> IRaceRepository:
    return RaceRepository(await get_db_session())


async def get_track_repository() -> ITrackRepository:
    return TrackRepository(await get_db_session())
