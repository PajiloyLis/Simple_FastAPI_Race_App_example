import uuid
from typing import Optional, List, Any, Coroutine

from Core.Models.Race import BaseRace, CreateRace, UpdateRace
from Core.Repository.IRaceRepository import IRaceRepository
from Core.Service.IRaceService import IRaceService


class RaceService(IRaceService):
    def __init__(self, race_repository: IRaceRepository):
        self.race_repository = race_repository

    async def get_race_in_season(self, season_id: uuid.UUID) -> List[BaseRace]:
        try:
            return await self.race_repository.get_race_in_season(season_id)
        except Exception as e:
            raise e

    async def get_by_id(self, id: uuid.UUID) -> Optional[BaseRace]:
        try:
            return await self.race_repository.get_by_id(id)
        except Exception as e:
            raise e

    async def get_all(self) -> List[BaseRace]:
        try:
            return await self.race_repository.get_all()
        except Exception as e:
            raise e

    async def create(self, race: CreateRace) -> BaseRace:
        try:
            return await self.race_repository.create(race)
        except Exception as e:
            raise e

    async def update(self, race: UpdateRace)->BaseRace:
        try:
            return await self.race_repository.update(race)
        except Exception as e:
            raise e

    async def delete(self, race_id: uuid.UUID) -> None:
        try:
            return await self.race_repository.delete(race_id)
        except Exception as e:
            raise e
