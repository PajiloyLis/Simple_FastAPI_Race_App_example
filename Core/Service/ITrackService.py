import uuid
from abc import ABC, abstractmethod
from typing import Optional, List

from Core.Models.Track.BaseTrack import BaseTrack
from Core.Models.Track.CreateTrack import CreateTrack
from Core.Models.Track.UpdateTrack import UpdateTrack
from Core.Repository.ITrackRepository import ITrackRepository


class ITrackService(ABC):
    @abstractmethod
    def __init__(self, track_repository: ITrackRepository):
        pass

    @abstractmethod
    async def get_by_id(self, id: uuid.UUID) -> Optional[BaseTrack]:
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def create(self, entity: CreateTrack) -> BaseTrack:
        pass

    @abstractmethod
    async def update(self, entity: UpdateTrack) -> BaseTrack:
        pass

    @abstractmethod
    async def delete(self, id: uuid.UUID) -> None:
        pass

    @abstractmethod
    async def get_all_tracks_in_country(self, country: str) -> List[BaseTrack]:
        pass