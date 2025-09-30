import uuid
from abc import abstractmethod
from typing import List, Optional
from abc import ABC, abstractmethod

from Core.Models.Race.BaseRace import BaseRace
from Core.Models.Race.CreateRace import CreateRace
from Core.Models.Race.UpdateRace import UpdateRace
from Core.Repository.IRaceRepository import IRaceRepository


class IRaceService(ABC):
    @abstractmethod
    def __init__(self, base_repository: IRaceRepository):
        pass

    @abstractmethod
    async def get_by_id(self, id: uuid.UUID) -> Optional[BaseRace]:
        pass

    @abstractmethod
    async def get_all(self) -> List[BaseRace]:
        pass

    @abstractmethod
    async def create(self, entity: CreateRace) -> BaseRace:
        pass

    @abstractmethod
    async def update(self, entity: UpdateRace) -> BaseRace:
        pass

    @abstractmethod
    async def delete(self, id: uuid.UUID) -> None:
        pass

    @abstractmethod
    async def get_race_in_season(self, season_id: uuid.UUID) -> List[BaseRace]:
        pass