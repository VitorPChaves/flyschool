from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, cpf: str, senha: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha
