class SeasonNotFoundException(Exception):
    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self) -> str:
        return self.__message

    def __str__(self):
        return self.message