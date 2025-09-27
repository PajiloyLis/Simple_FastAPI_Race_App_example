from sqlalchemy import (Column,
                        String,
                        DateTime,
                        UUID)
from BaseModel import BaseModel
from uuid import uuid4


class DriverPostgresDB(BaseModel):
    __table__ = "drivers"

    __id = Column(UUID, primary_key=True, default=uuid4)
    __name = Column(String, nullable=False)
    __surname = Column(String, nullable=False)
    __date_of_birth = Column(DateTime, nullable=False)
    __country = Column(String, nullable=False)

    def __init__(self, id: UUID, name: String, surname: String, date_of_birth: DateTime, country: String) -> None:
        if not isinstance(id, UUID):
            raise ValueError("id must be a UUID")
        if not isinstance(name, String):
            raise ValueError("name must be a String")
        if not isinstance(surname, String):
            raise ValueError("surname must be a String")
        if not isinstance(date_of_birth, DateTime):
            raise ValueError("date_of_birth must be a DateTime")
        if not isinstance(country, String):
            raise ValueError("country must be a String")

        super().__init__()
        __id = id
        __name = name
        __surname = surname
        __date_of_birth = date_of_birth
        __country = country

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def date_of_birth(self) -> DateTime:
        return self.__date_of_birth

    @property
    def country(self) -> str:
        return self.__country

    @name.setter
    def name(self, name: String) -> None:
        self.__name = name

    @surname.setter
    def surname(self, surname: String) -> None:
        self.__surname = surname

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: DateTime) -> None:
        self.__date_of_birth = date_of_birth

    @country.setter
    def country(self, country: String) -> None:
        self.__country = country
