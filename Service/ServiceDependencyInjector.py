from fastapi import Depends

from Core.Repository.IRaceRepository import IRaceRepository
from Core.Service.IRaceService import IRaceService
from Database.DatabaseDependencyInjector import get_race_repository
from Database.Repository.RacePostgresRepository import RaceRepository
from Service.RaceService import RaceService


def get_race_service(repository: IRaceRepository = Depends(get_race_repository)) -> RaceService:
    return RaceService(repository)
