import uuid
from sqlalchemy import (Column,
                        String)
from sqlalchemy.dialects.postgresql import UUID

from Database.Models.BaseModel import BaseModel


class TeamPostgresDB(BaseModel):
    __tablename__ = "teams"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    def __init__(self, id: uuid.UUID, name: str, country: str) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(name, str):
            raise ValueError("name must be of type String")
        if not isinstance(country, str):
            raise ValueError("country must be of type String")

        super().__init__()

        self.id = id
        self.name = name
        self.country = country