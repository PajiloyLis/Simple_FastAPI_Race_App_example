from pydantic import BaseModel, Field


class CreateSeasonDTO(BaseModel):
    year: int = Field(..., examples=[1990])