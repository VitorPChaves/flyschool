from src.entity.aluno import Aluno
from src.entity.nivel import Nivel
from src.entity.turno import Turno


class StudentController:
    def __init__(self):
        self.__alunos = []

        self.__aluno1 = Aluno('123.456.789-10', '123', 18, 70, Turno(1), Nivel(1))
        self.__aluno2 = Aluno('321.456.789-10', '123', 20, 90, Turno(2), Nivel(1))
        #self.__aluno3 = Aluno('111.456.789-10', '123', 30, 80, self.__nivel.EXPERIENTE)

        self.__alunos.append(self.__aluno1)

    def registered_students(self):
        return self.__alunos