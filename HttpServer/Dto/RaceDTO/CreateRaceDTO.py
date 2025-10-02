import datetime
import uuid
from pydantic import BaseModel, Field, validator, field_validator

from Core.Models.Race.CreateRace import CreateRace


class CreateRaceDTO(BaseModel):
    track_id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    season_id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    country: str = Field(..., examples=["Monaco"])
    laps_count: int = Field(..., ge=0, examples=[65])
    date: datetime.datetime = Field(..., examples=[datetime.datetime(year=2014, month=5, day=13, hour=14)])

    # def __init__(self, track_id: str, season_id: str, country: str, laps_count: int,
    #              date: str) -> None:
    #     if not isinstance(track_id, str):
    #         raise ValueError("track_id must be of type str")
    #     if not isinstance(season_id, str):
    #         raise ValueError("season_id must be of type str")
    #     if not isinstance(country, str):
    #         raise ValueError("country must be of type str")
    #     if not isinstance(laps_count, int) or laps_count <= 0:
    #         raise ValueError("laps_count must be of type int")
    #     if not isinstance(date, str):
    #         raise ValueError("date must be of type str")
    #
    #     self.track_id = uuid.UUID(track_id)
    #     self.season_id = uuid.UUID(season_id)
    #     self.country = country
    #     self.laps_count = laps_count
    #     self.date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")

    # @field_validator('track_id', 'season_id', mode='before')
    # @classmethod
    # def validate_uuid_strings(cls, value: str|uuid.UUID) -> uuid.UUID:
    #     if not isinstance(value, str|uuid.UUID):
    #         raise ValueError(f'Invalid UUID string: {value}')
    #     if isinstance(value, str):
    #         return uuid.UUID(value)
    #     else:
    #         return value
    #
    # @field_validator('date', mode='before')
    # @classmethod
    # def validate_date_string(cls, value: str | datetime.datetime):
    #     if not isinstance(value, str|datetime.datetime):
    #         raise ValueError(f'Invalid date string: {value}')
    #     if isinstance(value, str):
    #         return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    #     else:
    #         return value
    #
    # @field_validator('laps_count', mode='before')
    # @classmethod
    # def validate_laps_count(cls, v):
    #     if v < 1:
    #         raise ValueError("laps_count must be at least 1")
    #     return v
