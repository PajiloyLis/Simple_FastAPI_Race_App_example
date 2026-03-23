import uuid

from fastapi import APIRouter, HTTPException, status

from Core.Exceptions.SeasonAlreadyExistException import SeasonAlreadyExistException
from Core.Exceptions.SeasonNotFoundException import SeasonNotFoundException
from Core.Models.Season.SeasonConverter import convert_model_to_dto
from Core.Service.ISeasonService import ISeasonService
from HttpServer.Dto.SeasonDTO.SeasonDTO import SeasonDTO


class SeasonController:
    def __init__(self, season_service: ISeasonService):
        self.router = APIRouter(prefix="/api/season", tags=["seasons"])

        self.season_service = season_service

    async def get_by_id(self, season_id: uuid.UUID) -> SeasonDTO:
        try:
            race = await self.season_service.get_by_id(season_id)
            if race is not None:
                return convert_model_to_dto(race)
            else:
                raise SeasonNotFoundException(f"Season with id {season_id} not found")
        except SeasonNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except SeasonAlreadyExistException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def get_by_year(self, year: int) -> SeasonDTO:
