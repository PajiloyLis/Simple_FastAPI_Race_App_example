import uuid
from abc import ABC, abstractmethod
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession

from Core.Models.Track.BaseTrack import BaseTrack
from Core.Models.Track.CreateTrack import CreateTrack
from Core.Models.Track.UpdateTrack import UpdateTrack


class ITrackRepository(ABC):
    @abstractmethod
    def __init__(self, session: AsyncSession):
        pass

    async def get_by_id(self, id: uuid.UUID)->Optional[BaseTrack]:
        pass

    async def create(self, track: CreateTrack)->BaseTrack:
        pass

    async def update(self, track: UpdateTrack)->BaseTrack:
        pass

    async def delete(self, id: uuid.UUID)->None:
        pass

    async def get_all(self)->List[BaseTrack]:
        pass

    async def get_all_tracks_in_country(self, country: str)->List[BaseTrack]:
        pass