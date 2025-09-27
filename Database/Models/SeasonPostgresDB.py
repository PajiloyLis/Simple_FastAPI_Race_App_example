from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime,
                        UUID)
from BaseModel import BaseModel
from uuid import uuid4

class SeasonPostgresDB(BaseModel):
    __tablename__ = 'seasons'

    __id = Column(UUID, primary_key=True, default=uuid4)
    __year = Column(DateTime, nullable=False)

    def __init__(self, id: UUID, year: DateTime) -> None:
        if not isinstance(id, UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(year, DateTime):
            raise ValueError("year must be of type DateTime")

        super().__init__()

        __id = id
        __year = year

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def year(self) -> DateTime:
        return self.__year

    @year.setter
    def year(self, year: DateTime) -> None:
        self.__year = year