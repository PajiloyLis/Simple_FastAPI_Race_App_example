from sqlalchemy import (Column,
                        UUID,
                        String,
                        DOUBLE)
from BaseModel import BaseModel
from uuid import uuid4

class TrackPostgresDB(BaseModel):
    __tablename__ = 'tracks'

    __id = Column(UUID, primary_key=True, default=uuid4)
    __lap_length = Column(DOUBLE, nullable=False)
    __name = Column(String, nullable=False)
    __country = Column(String, nullable=False)

    def __init__(self, id, lap_length, name, country):
        if not isinstance(id, UUID):
            raise ValueError('id must be a UUID')
        if not isinstance(lap_length, DOUBLE) or lap_length <= 0.0:
            raise ValueError('lap_length must be a DOUBLE')
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        if not isinstance(country, str):
            raise ValueError('country must be a string')

        super().__init__()

        __id = id
        __lap_length = lap_length
        __name = name
        __country = country

    @property
    def id(self):
        return self.__id

    @property
    def lap_length(self):
        return self.__lap_length

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @lap_length.setter
    def lap_length(self, value: DOUBLE):
        lap_length = value

    @name.setter
    def name(self, value: String):
        name = value

    @country.setter
    def country(self, value: String):
        country = value
