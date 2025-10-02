from Core.Service.IRaceService import IRaceService
from Core.Service.ITrackService import ITrackService
from Database.DatabaseDependencyInjector import get_race_repository, get_track_repository
from Service.RaceService import RaceService
from Service.TrackService import TrackService


async def get_race_service() -> IRaceService:
    return RaceService(await get_race_repository())


async def get_track_service() -> ITrackService:
    return TrackService(await get_track_repository())
