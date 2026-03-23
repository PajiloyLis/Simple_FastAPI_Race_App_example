import uuid
from typing import List

from fastapi import APIRouter, Path, Body, status, HTTPException
from starlette.responses import JSONResponse

from Core.Exceptions.TrackAlreadyExistException import TrackAlreadyExistException
from Core.Exceptions.TrackNotFoundException import TrackNotFoundException
from Core.Models.Track.TrackConverter import convert_model_to_dto, convert_dto_to_create, convert_dto_to_update
from Core.Service.ITrackService import ITrackService
from HttpServer.Dto.TrackDTO.CreateTrackDTO import CreateTrackDTO
from HttpServer.Dto.TrackDTO.TrackDTO import TrackDTO
from HttpServer.Dto.TrackDTO.UpdateTrackDTO import UpdateTrackDTO


class TrackController:
    def __init__(self, track_service: ITrackService):
        self.track_service = track_service
        self.router = APIRouter(prefix="/api/track", tags=["track"])
        self.router.add_api_route("/get_all", endpoint=self.get_all, methods=["GET"], response_model=List[TrackDTO])
        self.router.add_api_route("/get_all_in_country/{country}", endpoint=self.get_all_tracks_in_country,
                                  methods=["GET"], response_model=List[TrackDTO])
        self.router.add_api_route("/{track_id}", endpoint=self.get, methods=["GET"], response_model=TrackDTO)
        self.router.add_api_route("/create", endpoint=self.create, methods=["POST"], response_model=TrackDTO)
        self.router.add_api_route("/update", endpoint=self.update, methods=["PUT"], response_model=TrackDTO)
        self.router.add_api_route("/{track_id}", endpoint=self.delete, methods=["DELETE"], response_model=None)

    async def get(self, track_id: uuid.UUID = Path()) -> TrackDTO:
        try:
            track = await self.track_service.get_by_id(track_id)
            if track is None:
                raise TrackNotFoundException(f"Track with id {track_id} not found")
            else:
                return convert_model_to_dto(track)
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_all(self) -> List[TrackDTO]:
        try:
            tracks = await self.track_service.get_all()
            return [convert_model_to_dto(track) for track in tracks]
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_all_tracks_in_country(self, country: str = Path()) -> List[TrackDTO]:
        try:
            tracks = await self.track_service.get_all_tracks_in_country(country)
            return [convert_model_to_dto(track) for track in tracks]
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def create(self, dto: CreateTrackDTO = Body()) -> JSONResponse:
        try:
            track = await self.track_service.create(convert_dto_to_create(dto))
            return JSONResponse(content=convert_model_to_dto(track), status_code=status.HTTP_201_CREATED)
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def update(self, dto: UpdateTrackDTO = Body()) -> TrackDTO:
        try:
            track = await self.track_service.update(convert_dto_to_update(dto))
            return convert_model_to_dto(track)
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def delete(self, track_id: uuid.UUID = Path()) -> JSONResponse:
        try:
            await self.track_service.delete(track_id)
            return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)
        except TrackNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except TrackAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
