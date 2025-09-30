from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime)
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from Core.Models.Race.BaseRace import BaseRace
from BaseModel import BaseModel


class RacePostgresDB(BaseModel):
    __tablename__ = 'races'

    id = Column(UUID, as_uuid=True, primary_key=True, default=uuid4)
    track_id = Column(UUID, ForeignKey('tracks.id'))
    date = Column(DateTime, nullable=False)
    laps_count = Column(Integer, default=0, nullable=False)
    season_id = Column(UUID, ForeignKey('seasons.id'))
    country = Column(String, nullable=False)

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

        self.id = id
        self.track_id = track_id
        self.date = date
        self.laps_count = laps_count
        self.season_id = season_id
        self.country = country

    def convert_postgres(self) -> BaseRace:
        return BaseRace(self.id, self.track_id, self.date, self.laps_count, self.season_id, self.country)
