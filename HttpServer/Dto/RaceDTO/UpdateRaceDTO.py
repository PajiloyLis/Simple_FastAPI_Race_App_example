import datetime
import uuid
from pydantic import BaseModel, Field, validator
from Core.Models.Race.UpdateRace import UpdateRace


class UpdateRaceDTO(BaseModel):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    track_id: uuid.UUID | None = Field(..., examples=[uuid.uuid4()])
    season_id: uuid.UUID | None = Field(..., examples=[uuid.uuid4()])
    country: str | None = Field(..., examples=["Monaco"])
    laps_count: int | None = Field(..., ge=0, examples=[65])
    date: datetime.datetime | None = Field(..., examples=[datetime.datetime(year=2014, month=5, day=13, hour=14)])

    def __init__(self, id: uuid.UUID, track_id: uuid.UUID | None, season_id: uuid.UUID | None, country: str | None, laps_count: int | None,
                 date: datetime.datetime | None) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type uuid.UUID")
        if not isinstance(track_id, uuid.UUID | None):
            raise ValueError("track_id must be of type uuid.UUID")
        if not isinstance(season_id, uuid.UUID | None):
            raise ValueError("season_id must be of type uuid.UUID")
        if not isinstance(country, str | None):
            raise ValueError("country must be of type str")
        if not isinstance(laps_count, int | None) or laps_count <= 0:
            raise ValueError("laps_count must be of type int")
        if not isinstance(date, datetime.datetime | None) or date > datetime.datetime.now():
            raise ValueError("date must be of type datetime.datetime")

        self.id = id
        self.track_id = track_id
        self.season_id = season_id
        self.country = country
        self.laps_count = laps_count
        self.date = date

    def convert(self) -> UpdateRace:
        return UpdateRace(self.id, self.track_id, self.date, self.laps_count, self.season_id, self.country)
