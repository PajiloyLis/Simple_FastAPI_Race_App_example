from typing import Optional, Any, Coroutine
from fastapi import APIRouter, FastAPI, Query, HTTPException, status
import uuid

from Core.Exceptions.RaceAlreadyExistException import RaceAlreadyExistException
from Core.Exceptions.RaceNotFoundException import RaceNotFoundException
from Core.Models.Race.BaseRace import BaseRace
from Core.Service.IRaceService import IRaceService
from HttpServer.Dto.RaceDTO.RaceDTO import RaceDTO


class RaceController:
    def __init__(self, race_service: IRaceService):
        self.router = APIRouter(prefix="api/race", tags=["races"])
        self.router.add_api_route("/{race_id}", endpoint=self.get, methods=["GET"], response_model=RaceDTO)
        self.race_service = race_service

    async def get(self, id: uuid.UUID = Query(ge=0)) -> RaceDTO | None:
        try:
            race: BaseRace = await self.race_service.get_by_id(id)
            if race is not None:
                race_to_return = race.convert()
        except RaceNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except RaceAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
