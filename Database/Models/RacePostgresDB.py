import datetime
import uuid
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime)
from sqlalchemy.dialects.postgresql import UUID


from Database.Models.BaseModel import BaseModel


class RacePostgresDB(BaseModel):
    __tablename__ = 'races'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    track_id = Column(UUID, ForeignKey('tracks.id'))
    date = Column(DateTime, nullable=False)
    laps_count = Column(Integer, default=0, nullable=False)
    season_id = Column(UUID, ForeignKey('seasons.id'))
    country = Column(String, nullable=False)

    def __init__(self, id: uuid.UUID, track_id: uuid.UUID, date: datetime.datetime, laps_count: int, season_id: uuid.UUID, country: str):
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(track_id, uuid.UUID):
            raise ValueError("track_id must be of type UUID")
        if not isinstance(date, datetime.datetime):
            raise ValueError("date must be of type DateTime")
        if not isinstance(laps_count, int) or laps_count <= 0:
            raise ValueError("laps_count must be of type Integer")
        if not isinstance(season_id, uuid.UUID):
            raise ValueError("season_id must be of type UUID")
        if not isinstance(country, str):
            raise ValueError("country must be of type String")

        super().__init__()

        self.id = id
        self.track_id = track_id
        self.date = date
        self.laps_count = laps_count
        self.season_id = season_id
        self.country = country