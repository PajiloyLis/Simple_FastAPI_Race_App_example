from fastapi import APIRouter, HTTPException, status, Body, Path
import uuid

from starlette.responses import JSONResponse

from Core.Exceptions.RaceAlreadyExistException import RaceAlreadyExistException
from Core.Exceptions.RaceNotFoundException import RaceNotFoundException
from Core.Service.IRaceService import IRaceService
from HttpServer.Dto.RaceDTO.CreateRaceDTO import CreateRaceDTO
from HttpServer.Dto.RaceDTO.RaceDTO import RaceDTO
from Core.Models.Race.RaceConverter import convert_model_to_dto, convert_dto_to_create


class RaceController:
    def __init__(self, race_service: IRaceService):
        self.router = APIRouter(prefix="/api/race", tags=["races"])
        self.router.add_api_route("/{race_id}", endpoint=self.get, methods=["GET"], response_model=RaceDTO)
        self.router.add_api_route("/create", endpoint=self.create, methods=["POST"], response_model=RaceDTO)
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