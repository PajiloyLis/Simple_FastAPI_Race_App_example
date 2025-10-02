import datetime
import uuid
from pydantic import BaseModel, Field

class RaceDTO(BaseModel):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    track_id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    season_id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    country: str = Field(..., examples=["Monaco"])
    laps_count: int = Field(..., ge=0, examples=[65])
    date: datetime.datetime = Field(..., examples=[datetime.datetime(year=2014, month=5, day=13, hour=14)])
