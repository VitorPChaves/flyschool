from src.entity.abstract.atleta import Atleta
from src.entity.day import Day
from src.entity.turno import Turno


class Professor(Atleta):
    def __init__(self, cpf: str, senha: str, idade: int, peso: int, turno: Turno, disponivel: bool, day: Day):
        super().__init__(cpf, senha, idade, peso, turno)
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
        if isinstance(day, Day):
            self.__day = day

    @property
    def disponivel(self) -> bool:
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel

    @property
    def day(self) -> Day:
        return self.__day

    @day.setter
    def day(self, day: Day):
        if isinstance(day, Day):
            self.__day = day
