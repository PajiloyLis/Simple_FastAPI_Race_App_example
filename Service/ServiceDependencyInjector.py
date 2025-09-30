from fastapi import Depends

from Core.Repository.IRaceRepository import IRaceRepository
from Core.Service.IRaceService import IRaceService
from Database.DatabaseDependencyInjector import get_race_repository
from Service.RaceService import RaceService


async def get_race_service(repository: IRaceRepository = Depends(get_race_repository)) -> IRaceService:
    return RaceService(repository)
