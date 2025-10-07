import uuid


class BaseSeason:
    def __init__(self, id: uuid.UUID, year: int) -> None:
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type uuid.UUID")
        if not isinstance(year, int) or year < 1950:
            raise ValueError("year must be of type int and greater or equal than 1950")

        self.id = id
        self.year = year
