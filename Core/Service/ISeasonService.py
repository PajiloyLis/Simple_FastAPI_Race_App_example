import uuid
from abc import ABC, abstractmethod
from typing import List

from Core.Models.Season.BaseSeason import BaseSeason
from Core.Models.Season.CreateSeason import CreateSeason
from Core.Models.Season.UpdateSeason import UpdateSeason
from Core.Repository.ISeasonRepository import ISeasonRepository


class ISeasonService(ABC):
    @abstractmethod
    def __init(self, season_repository: ISeasonRepository):
        pass

    @abstractmethod
    async def get_by_id(self, id: uuid.UUID) -> BaseSeason:
        pass

    @abstractmethod
    async def get_all(self) -> List[BaseSeason]:
        pass

    @abstractmethod
    async def get_by_year(self, year: int) -> BaseSeason:
        pass

    @abstractmethod
    async def create(self, season: CreateSeason) -> BaseSeason:
        pass

    @abstractmethod
    async def update(self, season: UpdateSeason) -> BaseSeason:
        pass

    @abstractmethod
    async def delete(self, id: uuid.UUID) -> None:
        pass
