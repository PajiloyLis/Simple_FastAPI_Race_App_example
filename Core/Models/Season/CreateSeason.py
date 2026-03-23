class CreateSeason:
    def __init__(self, year: int):
        if not isinstance(year, int) or year < 1950:
            raise ValueError("Year must be an integer and greater or equal than 1950")

        self.year = year
