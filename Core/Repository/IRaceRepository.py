from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.orm import Session
import uuid

from Core.Models.Race.BaseRace import BaseRace
from Core.Models.Race.CreateRace import CreateRace
from Core.Models.Race.UpdateRace import UpdateRace

T = TypeVar('T')

class IRaceRepository(ABC):
    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    async def get_race_in_season(self, season_id: uuid.UUID) -> List[BaseRace]:
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
