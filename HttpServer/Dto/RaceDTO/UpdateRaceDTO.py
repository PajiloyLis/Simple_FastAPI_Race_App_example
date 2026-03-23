import datetime
import uuid
from pydantic import BaseModel, Field


class UpdateRaceDTO(BaseModel):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    track_id: uuid.UUID | None = Field(..., examples=[uuid.uuid4()])
    season_id: uuid.UUID | None = Field(..., examples=[uuid.uuid4()])
    country: str | None = Field(..., examples=["Monaco"])
    laps_count: int | None = Field(..., ge=0, examples=[65])
    date: datetime.datetime | None = Field(..., examples=[datetime.datetime(year=2014, month=5, day=13, hour=14)])
