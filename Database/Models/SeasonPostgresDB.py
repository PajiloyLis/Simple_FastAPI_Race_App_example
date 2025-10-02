import uuid
from sqlalchemy import (Column,
                        Integer)
from sqlalchemy.dialects.postgresql import UUID

from Database.Models.BaseModel import BaseModel


class SeasonPostgresDB(BaseModel):
    __tablename__ = 'seasons'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    year = Column(Integer, nullable=False)

    def __init__(self, id: uuid.UUID, year: int) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(year, int):
            raise ValueError("year must be of type Integer")

        super().__init__()

        self.id = id
        self.year = year