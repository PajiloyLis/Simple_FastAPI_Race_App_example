from fastapi import Depends

from Core.Service.IRaceService import IRaceService
from HttpServer.Controller.RaceController import RaceController
from Service.ServiceDependencyInjector import get_race_service


async def get_race_controller(service: IRaceService = Depends(get_race_service)) -> RaceController:
    return RaceController(service)