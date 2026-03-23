import uuid

from Core.Models.Track.BaseTrack import BaseTrack
from Core.Models.Track.CreateTrack import CreateTrack
from Core.Models.Track.UpdateTrack import UpdateTrack
from Database.Models.TrackPostgresDB import TrackPostgresDB
from HttpServer.Dto.TrackDTO.CreateTrackDTO import CreateTrackDTO
from HttpServer.Dto.TrackDTO.TrackDTO import TrackDTO
from HttpServer.Dto.TrackDTO.UpdateTrackDTO import UpdateTrackDTO


def convert_model_to_postgres(entity: BaseTrack) -> TrackPostgresDB:
    return TrackPostgresDB(entity.id, entity.lap_length, entity.name, entity.country)


def convert_model_to_dto(entity: BaseTrack) -> TrackDTO:
    return TrackDTO(id=entity.id, lap_length=entity.lap_length, name=entity.name, country=entity.country)


def convert_postgres_to_model(entity: TrackPostgresDB) -> BaseTrack:
    return BaseTrack(entity.id, entity.name, entity.lap_length, entity.country)


def convert_create_to_postgres(entity: CreateTrack) -> TrackPostgresDB:
    return TrackPostgresDB(uuid.uuid4(), entity.lap_length, entity.name, entity.country)


def convert_dto_to_create(entity: CreateTrackDTO) -> CreateTrack:
    return CreateTrack(entity.name, entity.country, entity.lap_length)


def convert_dto_to_update(entity: UpdateTrackDTO) -> UpdateTrack:
    return UpdateTrack(entity.id, entity.name, entity.country, entity.lap_length)