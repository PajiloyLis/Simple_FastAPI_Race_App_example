import uuid

from pydantic import BaseModel, Field


class TrackDTO(BaseModel):
    id:  uuid.UUID  = Field(...,  examples=[uuid.uuid4()])
    lap_length: float = Field(..., examples=[5.65])
    name: str = Field(..., examples=["Monaco city circuit"])
    country: str = Field(..., examples=["Monaco"])