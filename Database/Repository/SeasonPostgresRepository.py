import uuid
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Core.Exceptions.SeasonAlreadyExistException import SeasonAlreadyExistException
from Core.Exceptions.SeasonNotFoundException import SeasonNotFoundException
from Core.Models.Season.BaseSeason import BaseSeason
from Core.Models.Season.CreateSeason import CreateSeason
from Core.Models.Season.SeasonConverter import convert_postgres_to_model, convert_create_to_postgres
from Core.Models.Season.UpdateSeason import UpdateSeason
from Core.Repository.ISeasonRepository import ISeasonRepository
from Database.Models.SeasonPostgresDB import SeasonPostgresDB


class SeasonRepository(ISeasonRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_by_id(self, id: uuid.UUID) ->BaseSeason:
        try:
            result = await self.__session.get(SeasonPostgresDB, id)
            if result is None:
                raise SeasonNotFoundException(f"Season with id {id} not found")
            return convert_postgres_to_model(result)
        except SeasonNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def get_by_year(self, year: int) ->BaseSeason:
        try:
            query = select(SeasonPostgresDB).where(SeasonPostgresDB.year == year)
            result = await self.__session.scalars(query)
            season = result.first()
            if season is None:
                raise SeasonNotFoundException(f"Season with year {year} not found")
            return convert_postgres_to_model(season)
        except SeasonNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def get_all(self) ->List[BaseSeason]:
        try:
            query = select(SeasonPostgresDB).order_by(SeasonPostgresDB.year)
            result = await self.__session.scalars(query)
            seasons = result.all()
            if seasons is None:
                raise SeasonNotFoundException(f"Seasons not found")
            return [convert_postgres_to_model(season) for season in seasons]
        except SeasonNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def create(self, entity: CreateSeason) ->BaseSeason:
        try:
            entity_to_add = convert_create_to_postgres(entity)
            duplicate = await self.__check_duplicates_without_id(entity_to_add)
            if duplicate is not None:
                raise SeasonAlreadyExistException(f"Season with such year and id {duplicate.id} already exists")
            self.__session.add(entity_to_add)
            await self.__session.commit()
            return convert_postgres_to_model(entity_to_add)
        except SeasonAlreadyExistException as e:
            raise e
        except Exception as e:
            raise e

    async def update(self, entity: UpdateSeason) ->BaseSeason:
        try:
            to_merge = await self.__session.get(SeasonPostgresDB, entity.id)
            if to_merge is None:
                raise SeasonNotFoundException(f"Season with id {entity.id} not found")

            to_merge.year = entity.year if entity.year is not None else to_merge.year

            duplicate = await self.__check_duplicates_without_id(to_merge)
            if duplicate is not None:
                raise SeasonAlreadyExistException(f"Season with such year and id {duplicate.id} already exists")

            merged = await self.__session.merge(to_merge)
            await self.__session.commit()
            return convert_postgres_to_model(merged)
        except SeasonNotFoundException as e:
            raise e
        except SeasonAlreadyExistException as e:
            raise e
        except Exception as e:
            raise e

    async def delete(self, id: uuid.UUID) ->None:
        try:
            entity_to_delete = await self.__session.get(SeasonPostgresDB, id)
            if entity_to_delete is None:
                raise SeasonNotFoundException(f"Season with id {id} not found")
            await self.__session.delete(entity_to_delete)
            await self.__session.commit()
        except SeasonNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def __check_duplicates_without_id(self, entity: SeasonPostgresDB) -> Optional[SeasonPostgresDB]:
        query = select(SeasonPostgresDB).where(SeasonPostgresDb.year == entity.year)
        result = await self.__session.scalars(query)
        return result.first()