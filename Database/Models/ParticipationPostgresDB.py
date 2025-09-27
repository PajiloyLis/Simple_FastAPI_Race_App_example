from uuid import uuid4

from sqlalchemy import (Column,
                        ForeignKey,
                        String,
                        Integer,
                        DateTime,
                        UUID)
from BaseModel import BaseModel

class ParticipationPostgresDB(BaseModel):
    __tablename__ = 'participations'

    __id = Column(UUID, primary_key=True, default=uuid4)
    __race_id = Column(UUID, ForeignKey('races.id'))
    __driver_id = Column(UUID, ForeignKey('drivers.id'))
    __team_id = Column(UUID, ForeignKey('teams.id'))
    __laps_passed = Column(Integer, nullable = False)
    __start_position = Column(Integer, nullable = True)
    __finish_position = Column(Integer, nullable = True)
    __points = Column(Integer, nullable = True)

    def __init__(self, id: UUID, race_id: UUID, driver_id: UUID, team_id: UUID, laps_passed: Integer, start_position: Integer, finish_position: Integer, points: Integer) -> None:
        super().__init__()

        if not isinstance(id, UUID):
            raise ValueError('id must be a UUID')
        if not isinstance(race_id, UUID):
            raise ValueError('race_id must be a UUID')
        if not isinstance(driver_id, UUID):
            raise ValueError('driver_id must be a UUID')
        if not isinstance(team_id, UUID):
            raise ValueError('team_id must be a UUID')
        if not isinstance(laps_passed, Integer) or laps_passed <= 0:
            raise ValueError('laps_passed must be of type Integer')
        if not isinstance(start_position, Integer) or start_position <= 0:
            raise ValueError('start_position must be of type Integer')
        if not isinstance(finish_position, Integer) or finish_position <= 0:
            raise ValueError('finish_position must be of type Integer')
        if not isinstance(points, Integer) or points <= 0:
            raise ValueError('points must be of type Integer')

        __id = id
        __race_id = race_id
        __driver_id = driver_id
        __team_id = team_id
        __laps_passed = laps_passed
        __start_position = start_position
        __finish_position = finish_position
        __points = points

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def race_id(self) -> UUID:
        return self.__race_id

    @property
    def driver_id(self) -> UUID:
        return self.__driver_id

    @property
    def team_id(self) -> UUID:
        return self.__team_id

    @property
    def laps_passed(self) -> Integer:
        return self.__laps_passed

    @property
    def start_position(self) -> Integer:
        return self.__start_position

    @property
    def finish_position(self) -> Integer:
        return self.__finish_position

    @property
    def points(self) -> Integer:
        return self.__points

    @laps_passed.setter
    def laps_passed(self, laps_passed: Integer) -> None:
        self.__laps_passed = laps_passed

    @start_position.setter
    def start_position(self, start_position: Integer) -> None:
        self.__start_position = start_position

    @finish_position.setter
    def finish_position(self, finish_position: Integer) -> None:
        self.__finish_position = finish_position

    @points.setter
    def points(self, points: int) -> None:
        self.__points = points
