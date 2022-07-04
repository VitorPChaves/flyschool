from src.entity.aluno import Aluno
from src.entity.paraquedas import Paraquedas
from src.entity.turno import Turno


class Aula:
    def __init__(self, aluno: Aluno, turno: Turno, paraquedas: Paraquedas, dia: str):
        if isinstance(aluno, Aluno):
            self.__aluno = aluno
        if isinstance(turno, Turno):
            self.__turno = turno
        if isinstance(paraquedas, Paraquedas):
            self.__paraquedas = paraquedas
        if isinstance(dia, int):
            self.__dia = dia

    @property
    def aluno(self) -> Aluno:
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__aluno = aluno

    @property
    def turno(self) -> Turno:
        return self.__turno

    @turno.setter
    def turno(self, turno: Turno):
        if isinstance(turno, Turno):
            self.__turno = turno

    @property
    def paraquedas(self) -> Paraquedas:
        return self.__paraquedas

    @paraquedas.setter
    def paraquedas(self, paraquedas: Paraquedas):
        if isinstance(paraquedas, Paraquedas):
            self.__paraquedas = paraquedas

    @property
    def dia(self) -> str:
        return self.__dia

    @dia.setter
    def dia(self, dia: str):
        if isinstance(dia, str):
            self.__dia = dia