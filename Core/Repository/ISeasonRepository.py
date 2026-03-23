import uuid
from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from Core.Models.Season.BaseSeason import BaseSeason
from Core.Models.Season.CreateSeason import CreateSeason
from Core.Models.Season.UpdateSeason import UpdateSeason


class ISeasonRepository(ABC):
    @abstractmethod
    def __init__(self, session: AsyncSession) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, id: uuid.UUID)->BaseSeason:
        pass

    @abstractmethod
    async def get_by_year(self, year: int)->BaseSeason:
        pass

    @abstractmethod
    async def get_all(self)->List[BaseSeason]:
        pass

    @abstractmethod
    async def create(self, entity: CreateSeason)->BaseSeason:
        pass

    @abstractmethod
    async def update(self, entity: UpdateSeason)->BaseSeason:
        pass

    @abstractmethod
    async def delete(self, id: uuid.UUID)->None:
        pass