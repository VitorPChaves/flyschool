from src.entity.abstract.atleta import Atleta
from src.entity.nivel import Nivel


class Aluno(Atleta):

    def __init__(self, cpf: str, senha: str, idade: int, peso: int, nivel: Nivel):
        super().__init__(cpf, senha, idade, peso)
        if isinstance(nivel, Nivel):
            self.__nivel = nivel

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel
