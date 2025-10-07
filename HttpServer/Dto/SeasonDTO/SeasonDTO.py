import uuid
from pydantic import BaseModel, Field


class SeasonDTO(BaseModel):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    year: int = Field(..., examples=[1999])