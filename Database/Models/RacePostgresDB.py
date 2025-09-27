import uuid

from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime,
                        UUID)

from BaseModel import BaseModel
from uuid import uuid4

class RacePostgresDB(BaseModel):
    __tablename__ = 'races'

    __id = Column(UUID, primary_key=True, default=uuid4)
    __track_id = Column(UUID, ForeignKey('tracks.id'))
    __date=Column(DateTime, nullable=False)
    __laps_count = Column(Integer, default=0, nullable=False)
    __season_id = Column(UUID, ForeignKey('seasons.id'))
    __country = Column(String, nullable=False)

    def __init__(self, id: UUID, track_id: UUID, date: DateTime, laps_count: Integer, season_id: UUID, country: String):
        if not isinstance(id, UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(track_id, UUID):
            raise ValueError("track_id must be of type UUID")
        if not isinstance(date, DateTime):
            raise ValueError("date must be of type DateTime")
        if not isinstance(laps_count, Integer) or laps_count <= 0:
            raise ValueError("laps_count must be of type Integer")
        if not isinstance(season_id, UUID):
            raise ValueError("season_id must be of type UUID")
        if not isinstance(country, String):
            raise ValueError("country must be of type String")

        super().__init__()

        self.__id = id
        self.__track_id = track_id
        self.__date = date
        self.__laps_count = laps_count
        self.__season_id = season_id
        self.__country = country

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def track_id(self) -> UUID:
        return self.__track_id

    @property
    def date(self) -> DateTime:
        return self.__date

    @property
    def laps_count(self) -> Integer:
        return self.__laps_count

    @property
    def season_id(self) -> UUID:
        return self.__season_id

    @property
    def country(self) -> String:
        return self.__country

    @date.setter
    def date(self, date: DateTime):
        self.__date = date

    @laps_count.setter
    def laps_count(self, laps_count: Integer):
        self.__laps_count = laps_count

    @country.setter
    def country(self, country: String):
        self.__country = country
