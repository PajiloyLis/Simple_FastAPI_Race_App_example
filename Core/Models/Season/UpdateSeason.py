import uuid


class UpdateSeason:
    def __init__(self, id: uuid.UUID, year: int|None):
        if not isinstance(year, int) or (year is not None and year < 1950):
            raise ValueError("year must be an integer and greater or equal than 1950")
        if not isinstance(id, uuid.UUID):
            raise ValueError("id must be of type uuid.UUID")

        self.id = id
        self.year = year
