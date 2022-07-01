from src.entity.abstract.atleta import Atleta


class Paraquedas:
    def __init__(self, cor: str, status: bool):
        if isinstance(cor, str):
            self.__cor = cor
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
