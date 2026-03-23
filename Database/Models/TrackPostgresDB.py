import uuid
from sqlalchemy import (Column,
                        String,
                        Float)
from sqlalchemy.dialects.postgresql import UUID

from Database.Models.BaseModel import BaseModel


class TrackPostgresDB(BaseModel):
    __tablename__ = 'tracks'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    lap_length = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    def __init__(self, id: uuid.UUID, lap_length: float, name: str, country: str):
        if not isinstance(id, uuid.UUID):
            raise ValueError('id must be a UUID')
        if not isinstance(lap_length, (int, float)) or lap_length <= 0.0:
            raise ValueError('lap_length must be a positive number')
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        if not isinstance(country, str):
            raise ValueError('country must be a string')

        super().__init__()

        self.id = id
        self.lap_length = lap_length
        self.name = name
        self.country = country
