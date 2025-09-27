from  sqlalchemy import (Column,
                         String,
                         UUID)
from uuid import uuid4
from BaseModel import BaseModel


class TeamPostgresDB(BaseModel):
    __tablename__ = "teams"

    __id = Column(UUID, primary_key=True, default=uuid4)
    __name = Column(String, nullable=False)
    __country = Column(String, nullable=False)

    def __init__(self, id: UUID, name: str, country: String) -> None:
        if not isinstance(id, UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(name, str):
            raise ValueError("name must be of type String")
        if not isinstance(country, str):
            raise ValueError("country must be of type String")

        super().__init__()

        __id = id
        __name = name
        __country = country

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: String) -> None:
        self.__country = country

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name