from src.entity.abstract.atleta import Atleta
from src.entity.day import Day


class Paraquedas:
    def __init__(self, cor: str, status: bool, day: Day):
        if isinstance(cor, str):
            self.__cor = cor
        if isinstance(day, Day):
            self.__day = day
        if isinstance(status, bool):
            self.__status = status

    @property
    def cor(self) -> str:
        return self.__cor

    @cor.setter
    def cor(self, cor: str):
        if isinstance(cor, int):
            self.__cor = cor

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool):
        if isinstance(status, bool):
            self.__status = status

    @property
    def day(self) -> Day:
        return self.__day

    @day.setter
    def day(self, day: Day):
        if isinstance(day, Day):
            self.__day = day