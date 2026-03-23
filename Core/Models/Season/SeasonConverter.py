import uuid

from Core.Models.Season.BaseSeason import BaseSeason
from Core.Models.Season.CreateSeason import CreateSeason
from Core.Models.Season.UpdateSeason import UpdateSeason
from Database.Models.SeasonPostgresDB import SeasonPostgresDB
from HttpServer.Dto.SeasonDTO.CreateSeasonDTO import CreateSeasonDTO
from HttpServer.Dto.SeasonDTO.SeasonDTO import SeasonDTO
from HttpServer.Dto.SeasonDTO.UpdateSeasonDTO import UpdateSeasonDTO


def convert_model_to_postgres(entity: BaseSeason) -> SeasonPostgresDB:
    return SeasonPostgresDB(entity.id, entity.year)


def convert_model_to_dto(entity: BaseSeason) -> SeasonDTO:
    return SeasonDTO(id=entity.id, year=entity.year)


def convert_postgres_to_model(entity: SeasonPostgresDB) -> BaseSeason:
    return BaseSeason(id=entity.id, year=entity.year)


def convert_create_to_postgres(entity: CreateSeason) -> SeasonPostgresDB:
    return SeasonPostgresDB(uuid.uuid4(), entity.year)


def convert_dto_to_create(entity: CreateSeasonDTO) -> CreateSeason:
    return CreateSeason(entity.year)


def convert_dto_to_update(entity: UpdateSeasonDTO) -> UpdateSeason:
    return UpdateSeason(entity.id, entity.year)
