import uuid

from Core.Models.Race.BaseRace import BaseRace
from Core.Models.Race.CreateRace import CreateRace
from Core.Models.Race.UpdateRace import UpdateRace
from Database.Models.RacePostgresDB import RacePostgresDB
from HttpServer.Dto.RaceDTO.CreateRaceDTO import CreateRaceDTO
from HttpServer.Dto.RaceDTO.RaceDTO import RaceDTO
from HttpServer.Dto.RaceDTO.UpdateRaceDTO import UpdateRaceDTO


def convert_model_to_postgres(entity: BaseRace) -> RacePostgresDB:
    return RacePostgresDB(entity.id, entity.track_id, entity.date, entity.laps_count, entity.season_id, entity.country)


def convert_model_to_dto(entity: BaseRace) -> RaceDTO:
    return RaceDTO(id=entity.id, track_id=entity.track_id, season_id=entity.season_id, country=entity.country,
                   laps_count=entity.laps_count, date=entity.date)


def convert_postgres_to_model(entity: RacePostgresDB) -> BaseRace:
    return BaseRace(entity.id, entity.track_id, entity.date, entity.laps_count, entity.season_id, entity.country)


def convert_create_to_postgres(entity: CreateRace) -> RacePostgresDB:
    return RacePostgresDB(uuid.uuid4(), entity.track_id, entity.date, entity.laps_count, entity.season_id,
                          entity.country)


def convert_dto_to_create(entity: CreateRaceDTO) -> CreateRace:
    return CreateRace(entity.track_id, entity.date, entity.laps_count, entity.season_id, entity.country)


def convert_dto_to_update(entity: UpdateRaceDTO) -> UpdateRace:
    return UpdateRace(entity.id, entity.track_id, entity.date, entity.laps_count, entity.season_id, entity.country)
