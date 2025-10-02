from fastapi import Depends

from Core.Service.IRaceService import IRaceService
from Core.Service.ITrackService import ITrackService
from HttpServer.Controller.RaceController import RaceController
from HttpServer.Controller.TrackController import TrackController
from Service.ServiceDependencyInjector import get_race_service, get_track_service


async def get_race_controller() -> RaceController:
    return RaceController(await get_race_service())


async def get_track_controller() -> TrackController:
    return TrackController(await get_track_service())
