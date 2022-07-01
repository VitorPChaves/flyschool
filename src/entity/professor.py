from src.entity.abstract.atleta import Atleta
from src.entity.turno import Turno


class Professor(Atleta):
    def __init__(self, cpf: str, senha: str, idade: int, peso: int, disponivel: bool):
        super().__init__(cpf, senha, idade, peso)
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel

    @property
    def disponivel(self) -> bool:
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel

