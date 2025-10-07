import uuid
from typing import List

from Core.Models.Season.BaseSeason import BaseSeason
from Core.Models.Season.CreateSeason import CreateSeason
from Core.Models.Season.UpdateSeason import UpdateSeason
from Core.Repository.ISeasonRepository import ISeasonRepository
from Core.Service.ISeasonService import ISeasonService


class SeasonService(ISeasonService):
    def __init__(self, season_repository: ISeasonRepository):
        self.season_repository = season_repository

    async def get_by_id(self, id: uuid.UUID) -> BaseSeason:
        try:
            return await self.season_repository.get_by_id(id)
        except Exception as e:
            raise e

    async def get_by_year(self, year: int) -> BaseSeason:
        try:
            return await self.season_repository.get_by_year(year)
        except Exception as e:
            raise e

    async def get_all(self) -> List[BaseSeason]:
        try:
            return await self.season_repository.get_all()
        except Exception as e:
            raise e

    async def create(self, season: CreateSeason) -> BaseSeason:
        try:
            return await self.season_repository.create(season)
        except Exception as e:
            raise e

    async def update(self, season: UpdateSeason) -> BaseSeason:
        try:
            return await self.season_repository.update(season)
        except Exception as e:
            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            await self.season_repository.delete(id)
        except Exception as e:
            raise e