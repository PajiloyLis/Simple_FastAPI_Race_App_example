from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

from Core.Models.Race import CreateRace, UpdateRace, BaseRace
from Core.Repository.IRaceRepository import IRaceRepository
from Database.Models.RacePostgresDB import RacePostgresDB
from Core.Exceptions.RaceNotFoundException import RaceNotFoundException
from Core.Exceptions.RaceAlreadyExistException import RaceAlreadyExistException


class RaceRepository(IRaceRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, id: uuid.UUID) -> Optional[BaseRace]:
        try:
            result = await self._session.get(RacePostgresDB, id)
            if result is None:
                raise RaceNotFoundException(f"Race with id {id} not found")
            return result.convert_postgres()
        except Exception as e:
            raise e

    async def get_all(self) -> Optional[List[BaseRace]]:
        try:
            stmt = select(RacePostgresDB)
            result = await self._session.scalars(stmt)
            races = result.all()
            if races is not None:
                return [race.convert_postgres() for race in races]
        except Exception as e:
            raise e

    async def create(self, entity: CreateRace) -> BaseRace:
        try:
            entity_to_add = entity.convert_postgres()
            result = await self._session.get(RacePostgresDB, entity_to_add.id)
            if result is not None:
                raise RaceAlreadyExistException(f"Race with id {entity_to_add.id} already exists")
            self._session.add(entity_to_add)
            await self._session.flush()
            return entity_to_add.convert_postgres()
        except Exception as e:
            raise e

    async def update(self, entity: UpdateRace) -> BaseRace:
        try:
            to_merge = await self._session.get(RacePostgresDB, entity.id)
            if to_merge is None:
                raise RaceNotFoundException(f"Race with id {entity.id} not found")

            to_merge.track_id = entity.track_id if entity.track_id is not None else to_merge.track_id
            to_merge.laps_count = entity.laps_count if entity.laps_count is not None else to_merge.laps_count
            to_merge.date = entity.date if entity.date is not None else to_merge.date
            to_merge.country = entity.country if entity.country is not None else to_merge.country
            to_merge.season_id = entity.season_id if entity.season_id is not None else to_merge.season_id

            merged = await self._session.merge(entity)
            await self._session.flush()
            return merged
        except Exception as e:
            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            entity = await self.get_by_id(id)
            if entity:
                await self._session.delete(entity)
            else:
                raise RaceNotFoundException(f"Race with id {id} not found")
        except Exception as e:
            raise e

    async def get_race_in_season(self, season_id: uuid.UUID) -> Optional[List[BaseRace]]:
        try:
            stmt = select(RacePostgresDB).where(RacePostgresDB.season_id == season_id)
            result = await self._session.scalars(stmt)
            races = list(result.all())
            if races is not None:
                return [race.convert_postgres() for race in races]
        except Exception as e:
            raise e
