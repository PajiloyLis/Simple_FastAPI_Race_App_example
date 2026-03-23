from pydantic import BaseModel, Field


class CreateTrackDTO(BaseModel):
    lap_length: float = Field(..., examples=[5.65])
    name: str = Field(..., examples=["Monaco city circuit"])
    country: str = Field(..., examples=["Monaco"])