from src.entity.abstract.usuario import Usuario
from src.entity.turno import Turno


class Atleta(Usuario):
    def __init__(self, cpf: str, senha: str, idade: int, peso: int, turno: Turno):
        super().__init__(cpf, senha)
        if isinstance(idade, int):
            self.__idade = idade
        if isinstance(peso, int):
            self.__peso = peso
        if isinstance(turno, Turno):
            self.__turno = turno

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno
