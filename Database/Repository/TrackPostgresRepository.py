import uuid

from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Core.Exceptions.TrackAlreadyExistException import TrackAlreadyExistException
from Core.Exceptions.TrackNotFoundException import TrackNotFoundException
from Core.Models.Track.TrackConverter import convert_postgres_to_model, convert_create_to_postgres
from Core.Models.Track.BaseTrack import BaseTrack
from Core.Models.Track.CreateTrack import CreateTrack
from Core.Models.Track.UpdateTrack import UpdateTrack
from Core.Repository.ITrackRepository import ITrackRepository
from Database.Models.TrackPostgresDB import TrackPostgresDB


class TrackRepository(ITrackRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, id: int) -> BaseTrack:
        try:
            track = await self._session.get(TrackPostgresDB, id)
            if track is None:
                raise TrackNotFoundException(f"Track with id {id} not found")
            return convert_postgres_to_model(track)
        except TrackNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def create(self, track: CreateTrack) -> BaseTrack:
        try:
            entity_to_add = convert_create_to_postgres(track)
            duplicate = await self.__check_duplicate_without_id(entity_to_add)
            if duplicate is not None:
                raise TrackAlreadyExistException(
                    f"Another track with id {duplicate.id} and same parameters already exist")
            self._session.add(entity_to_add)
            await self._session.commit()
            return convert_postgres_to_model(entity_to_add)
        except TrackAlreadyExistException as e:
            raise e
        except Exception as e:
            raise e

    async def update(self, entity: UpdateTrack) -> BaseTrack:
        try:
            to_merge = await self._session.get(TrackPostgresDB, entity.id)
            if to_merge is None:
                raise TrackNotFoundException(f"Track with id {entity.id} not found")

            to_merge.country = entity.country if entity.country is not None else to_merge.country
            to_merge.lap_length = entity.lap_length if entity.lap_length is not None else to_merge.lap_length
            to_merge.name = entity.name if entity.name is not None else to_merge.name

            duplicate = await self.__check_duplicate_without_id(to_merge)

            if duplicate is not None:
                raise TrackAlreadyExistException(
                    f"Another track with id {duplicate.id} and same parameters already exist")

            merged = await self._session.merge(to_merge)
            await self._session.commit()
            return convert_postgres_to_model(merged)
        except TrackNotFoundException as e:
            raise e
        except TrackAlreadyExistException as e:
            raise e
        except Exception as e:
            raise e

    async def delete(self, id: uuid.UUID) -> None:
        try:
            entity = await self._session.get(TrackPostgresDB, id)
            if entity is None:
                raise TrackNotFoundException(f"Track with id {id} not found")
            await self._session.delete(entity)
            await self._session.commit()
        except TrackNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def get_all_tracks_in_country(self, country: str) -> List[BaseTrack]:
        try:
            query = select(TrackPostgresDB).where(TrackPostgresDB.country == country)
            result = await self._session.scalars(query)
            tracks = list(result.all())
            return [convert_postgres_to_model(track) for track in tracks]
        except Exception as e:
            raise e

    async def get_all(self) -> List[BaseTrack]:
        try:
            query = select(TrackPostgresDB)
            result = await self._session.scalars(query)
            tracks = result.all()
            if tracks is not None:
                return [convert_postgres_to_model(track) for track in tracks]
            else:
                raise TrackNotFoundException(f"Tracks not found")
        except TrackNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    async def __check_duplicate_without_id(self, track: TrackPostgresDB) -> TrackPostgresDB:
        query = select(TrackPostgresDB).where(TrackPostgresDB.lap_length == track.lap_length,
                                              TrackPostgresDB.country == track.country,
                                              TrackPostgresDB.name == track.name)
        result = await self._session.scalars(query)
        return result.first()
