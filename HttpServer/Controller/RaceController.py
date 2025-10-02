from typing import List

from fastapi import APIRouter, HTTPException, status, Body, Path
import uuid

from starlette.responses import JSONResponse

from Core.Exceptions.RaceAlreadyExistException import RaceAlreadyExistException
from Core.Exceptions.RaceNotFoundException import RaceNotFoundException
from Core.Service.IRaceService import IRaceService
from HttpServer.Dto.RaceDTO.CreateRaceDTO import CreateRaceDTO
from HttpServer.Dto.RaceDTO.RaceDTO import RaceDTO
from Core.Models.Race.RaceConverter import convert_model_to_dto, convert_dto_to_create, convert_dto_to_update
from HttpServer.Dto.RaceDTO.UpdateRaceDTO import UpdateRaceDTO


class RaceController:
    def __init__(self, race_service: IRaceService):
        self.router = APIRouter(prefix="/api/race", tags=["races"])
        self.router.add_api_route("/get_all", endpoint=self.get_all, methods=["GET"], response_model=List[RaceDTO])
        self.router.add_api_route("/get_all_in_season/{season_id}", endpoint=self.get_all_in_season, methods=["GET"], response_model=List[RaceDTO])
        self.router.add_api_route("/{race_id}", endpoint=self.get, methods=["GET"], response_model=RaceDTO)
        self.router.add_api_route("/create", endpoint=self.create, methods=["POST"], response_model=RaceDTO)
        self.router.add_api_route("/update", endpoint=self.update, methods=["PUT"], response_model=RaceDTO)
        self.race_service = race_service

    async def get(self, race_id: uuid.UUID = Path()) -> RaceDTO:
        try:
            race = await self.race_service.get_by_id(race_id)
            if race is not None:
                return convert_model_to_dto(race)
            else:
                raise RaceNotFoundException(f"Race {race_id} not found")
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def create(self, dto: CreateRaceDTO = Body()) -> JSONResponse:
        try:
            race = await self.race_service.create(convert_dto_to_create(dto))
            return JSONResponse(content=convert_model_to_dto(race), status_code=status.HTTP_201_CREATED)
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def update(self, dto: UpdateRaceDTO = Body()) -> RaceDTO:
        try:
            race = await self.race_service.update(convert_dto_to_update(dto))
            return convert_model_to_dto(race)
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_all(self) -> List[RaceDTO]:
        try:
            races = await self.race_service.get_all()
            return [convert_model_to_dto(race) for race in races]
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_all_in_season(self, season_id: uuid.UUID = Path()) -> List[RaceDTO]:
        try:
            races = await self.race_service.get_race_in_season(season_id)
            return [convert_model_to_dto(race) for race in races]
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
