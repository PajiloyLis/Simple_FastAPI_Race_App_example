import uuid
from typing import List

from watchfiles import awatch

from Core.Models.Track.BaseTrack import BaseTrack
from Core.Models.Track.CreateTrack import CreateTrack
from Core.Models.Track.UpdateTrack import UpdateTrack
from Core.Repository.ITrackRepository import ITrackRepository
from Core.Service.ITrackService import ITrackService


class TrackService(ITrackService):
    def __init__(self, track_repository: ITrackRepository) -> None:
        self.track_repository = track_repository

    async def get_by_id(self, id: uuid.UUID) -> BaseTrack:
        try:
            return await self.track_repository.get_by_id(id)
        except Exception as e:
            raise e

    async def get_all(self) -> List[BaseTrack]:
        try:
            return await self.track_repository.get_all()
        except Exception as e:
            raise e

    async def create(self, entity: CreateTrack) -> BaseTrack:
        try:
            return await self.track_repository.create(entity)
        except Exception as e:
            raise e

    async def update(self, entity: UpdateTrack) -> BaseTrack:
        try:
            return await self.track_repository.update(entity)
        except Exception as e:
            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            return await self.track_repository.delete(id)
        except Exception as e:
            raise e

    async def get_all_tracks_in_country(self, country: str) -> List[BaseTrack]:
        try:
            return await self.track_repository.get_all_tracks_in_country(country)
        except Exception as e:
            raise e
