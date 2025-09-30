from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Core.Repository.IRaceRepository import IRaceRepository
from Database.Database import Database
from Database.Repository.RacePostgresRepository import RaceRepository


async def get_db_session() -> AsyncSession:
    database = Database()
    if not database.is_connected:
        raise RuntimeError("Database is not connected")
    session = database.get_session()
    try:
        yield session
    finally:
        await session.close()

async def get_race_repository(session: AsyncSession = Depends(get_db_session)) -> IRaceRepository:
    return RaceRepository(session)