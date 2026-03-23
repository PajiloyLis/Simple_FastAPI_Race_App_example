import datetime
import uuid

from sqlalchemy import (Column,
                        String,
                        DateTime,
                        UUID)
from Database.Models.BaseModel import BaseModel
from uuid import uuid4


class DriverPostgresDB(BaseModel):
    __tablename__ = "drivers"

    id = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    country = Column(String, nullable=False)

    def __init__(self, id: uuid.UUID, name: str, surname: str, date_of_birth: datetime.datetime, country: str) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be a UUID")
        if not isinstance(name, str):
            raise ValueError("name must be a String")
        if not isinstance(surname, str):
            raise ValueError("surname must be a String")
        if not isinstance(date_of_birth, datetime.datetime):
            raise ValueError("date_of_birth must be a DateTime")
        if not isinstance(country, str):
            raise ValueError("country must be a String")

        super().__init__()

        self.id = id
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.country = country
