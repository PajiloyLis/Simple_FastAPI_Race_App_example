class RaceNotFoundException(Exception):
    def __init__(self, message: str):
            self.__message = message

    @property
    def message(self):
        return self.__message

    def __str__(self):
        return self.__message