import uuid


class UpdateTrack:
    def __init__(self, id: uuid.UUID, name: str | None, country: str | None, lap_length: float | None) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type UUID")
        if not isinstance(name, str | None):
            raise ValueError("name must be of type str or None")
        if not isinstance(country, str | None):
            raise ValueError("country must be of type str or None")
        if not isinstance(lap_length, float | None) or (lap_length is not None and lap_length <= 0):
            raise ValueError("lap_length must be of type float and greater than 0 or None")

        self.id = id
        self.name = name
        self.country = country
        self.lap_length = lap_length
