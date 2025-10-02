import uuid
from uuid import uuid4

from sqlalchemy import (Column,
                        ForeignKey,
                        String,
                        Integer,
                        DateTime,
                        UUID)
from Database.Models.BaseModel import BaseModel

class ParticipationPostgresDB(BaseModel):
    __tablename__ = 'participations'

    id = Column(UUID, primary_key=True, default=uuid4)
    race_id = Column(UUID, ForeignKey('races.id'))
    driver_id = Column(UUID, ForeignKey('drivers.id'))
    team_id = Column(UUID, ForeignKey('teams.id'))
    laps_passed = Column(Integer, nullable = False)
    start_position = Column(Integer, nullable = True)
    finish_position = Column(Integer, nullable = True)
    points = Column(Integer, nullable = False)

    def __init__(self, id: uuid.UUID, race_id: uuid.UUID, driver_id: uuid.UUID, team_id: uuid.UUID, laps_passed: int, start_position: int, finish_position: int, points: int) -> None:
        super().__init__()

        if not isinstance(id, uuid.UUID):
            raise ValueError('id must be a UUID')
        if not isinstance(race_id, uuid.UUID):
            raise ValueError('race_id must be a UUID')
        if not isinstance(driver_id, uuid.UUID):
            raise ValueError('driver_id must be a UUID')
        if not isinstance(team_id, uuid.UUID):
            raise ValueError('team_id must be a UUID')
        if not isinstance(laps_passed, int) or laps_passed <= 0:
            raise ValueError('laps_passed must be of type Integer')
        if not isinstance(start_position, int) or start_position <= 0:
            raise ValueError('start_position must be of type Integer')
        if not isinstance(finish_position, int) or finish_position <= 0:
            raise ValueError('finish_position must be of type Integer')
        if not isinstance(points, int) or points <= 0:
            raise ValueError('points must be of type Integer')

        self.id = id
        self.race_id = race_id
        self.driver_id = driver_id
        self.team_id = team_id
        self.laps_passed = laps_passed
        self.start_position = start_position
        self.finish_position = finish_position
        self.points = points
