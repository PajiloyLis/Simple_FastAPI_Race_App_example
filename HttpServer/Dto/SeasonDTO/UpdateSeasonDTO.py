import uuid

from pydantic import BaseModel, Field


class UpdateSeasonDTO(BaseModel):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    year: int | None = Field(..., examples=[1999])
