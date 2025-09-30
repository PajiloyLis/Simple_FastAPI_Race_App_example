import uuid
from datetime import datetime, date

from Database.Models.RacePostgresDB import RacePostgresDB


class CreateRace:
    def __init__(self, track_id: uuid.UUID, date: datetime, laps_count: int, season_id: uuid.UUID, country: str) -> None:
        if not isinstance(date, datetime) or date > datetime.now():
            raise ValueError("date must be of type datetime")
        if not isinstance(laps_count, int) or laps_count <= 0:
            raise ValueError("laps_count must be of type int")
        if not isinstance(season_id, uuid.UUID):
            raise ValueError("season_id must be of type UUID")
        if not isinstance(country, str):
            raise ValueError("country must be of type str")

        self.track_id = track_id
        self.date = date
        self.laps_count = laps_count
        self.season_id = season_id
        self.country = country

    def convert_postgres(self) -> RacePostgresDB:
        return RacePostgresDB(uuid.uuid4(), self.track_id, self.date, self.laps_count, self.season_id, self.country)
