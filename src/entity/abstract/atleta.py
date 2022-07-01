from src.entity.abstract.usuario import Usuario


class Atleta(Usuario):
    def __init__(self, cpf: str, senha: str, idade: int, peso: int):
        super().__init__(cpf, senha)
        if isinstance(idade, int):
            self._idade = idade
        if isinstance(peso, int):
            self._peso = peso

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self.idade = idade

    @property
    def peso(self):
        return self.peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso
