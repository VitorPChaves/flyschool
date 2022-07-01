from src.entity.aluno import Aluno


class StudentController:
    def __init__(self):
        self.__aluno = Aluno()
        self.__alunos = []

        self.__aluno1 = Aluno('123.456.789-10', '123', 18, 70, self.__nivel.INICIANTE)
        self.__aluno2 = Aluno('321.456.789-10', '123', 20, 90, self.__nivel.INICIANTE)
        self.__aluno3 = Aluno('111.456.789-10', '123', 30, 80, self.__nivel.EXPERIENTE)

        self.__alunos.append()

    def registered_students(self):
        return self.__alunos