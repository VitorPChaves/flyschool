from .abstractDAO import abstractDAO
from src.entity import Aluno

class AlunoDAO(abstractDAO):
    def __init__(self):
        super().__init__('student_list.pkl')

    def adicionar_aluno(self, aluno: Aluno):
        super().adicionar(aluno.cpf, aluno)

    def capturar_aluno(self, aluno: Aluno):
        return super().capturar(aluno.cpf)

    def remover_aluno(self, chave):
        return super().remover(chave)
