import uuid


class BaseTrack:
    def __init__(self, id: uuid.UUID, name: str, lap_length: float, country: str) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type uuid.UUID")
        if not isinstance(name, str):
            raise ValueError("name must be of type str")
        if not isinstance(lap_length, float) or lap_length <= 0:
            raise ValueError("lap_length must be of type float or greater than 0")
        if not isinstance(country, str):
            raise ValueError("country must be of type str")

        self.id = id
        self.name = name
        self.lap_length = lap_length
        self.country = country
