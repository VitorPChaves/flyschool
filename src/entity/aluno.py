from src.entity.abstract.atleta import Atleta
from src.entity.day import Day
from src.entity.nivel import Nivel
from src.entity.turno import Turno


class Aluno(Atleta):

    def __init__(self, cpf: str, senha: str, idade: int, peso: int, turno: Turno, nivel: Nivel, day: Day):
        super().__init__(cpf, senha, idade, peso, turno)
        if isinstance(nivel, Nivel):
            self.__nivel = nivel
        if isinstance(day, Day):
            self.__day = day

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def day(self) -> Day:
        return self.__day

    @day.setter
    def day(self, day: Day):
        if isinstance(day, Day):
            self.__day = day
