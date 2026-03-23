import uuid

from pydantic import BaseModel, Field


class UpdateTrackDTO(BaseModel):
    id:  uuid.UUID  = Field(...,  examples=[uuid.uuid4()])
    lap_length: float | None = Field(..., examples=[5.65])
    name: str | None = Field(..., examples=["Monaco city circuit"])
    country: str | None = Field(..., examples=["Monaco"])