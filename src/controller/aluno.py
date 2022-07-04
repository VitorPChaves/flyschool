from src.entity.aluno import Aluno
from src.entity.day import Day
from src.entity.nivel import Nivel
from src.entity.turno import Turno


class StudentController:
    def __init__(self):
        self.__alunos = []

        self.__aluno1 = Aluno('123.456.789-10', '123', 18, 70, Turno(), Nivel(1), Day())
        self.__aluno2 = Aluno('321.456.789-10', '123', 20, 90, Turno(), Nivel(2), Day())
        #self.__aluno3 = Aluno('111.456.789-10', '123', 30, 80, self.__nivel.EXPERIENTE)

        self.__alunos.append(self.__aluno1)
        self.__alunos.append(self.__aluno2)

    def registered_students(self):
        return self.__alunos