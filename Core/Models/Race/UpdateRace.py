import uuid
from datetime import datetime


class UpdateRace:
    def __init__(self, id: uuid.UUID, track_id: uuid.UUID | None, date: datetime | None, laps_count: int | None, season_id: uuid.UUID | None, country: str | None) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type uuid.UUID")
        if not isinstance(date, datetime | None):
            raise ValueError("date must be of type datetime")
        if not isinstance(laps_count, int | None) or (laps_count is not None and laps_count <= 0):
            raise ValueError("laps_count must be of type int")
        if not isinstance(season_id, uuid.UUID | None):
            raise ValueError("season_id must be of type UUID")
        if not isinstance(country, str | None):
            raise ValueError("country must be of type str")
        if not isinstance(season_id, uuid.UUID | None):
            raise ValueError("season_id must be of type UUID")

        self.id = id
        self.track_id = track_id
        self.date = date
        self.laps_count = laps_count
        self.season_id = season_id
        self.country = country


