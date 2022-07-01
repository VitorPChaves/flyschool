from src.entity.professor import Professor


class InstructorController:
    def __init__(self):
        self.__instructor = Professor()
        self.__instructors = []

        self.__professor1 = Professor('567.456.789-10', '123', 18, 70, True)
        self.__professor2 = Professor('765.456.789-10', '123', 20, 90, True)

        self.__instructors.append(self.__professor1)
        self.__instructors.append(self.__professor2)

    def registered_teachers(self):
        return self.__instructors

    def check_teachers(self):
        for instructor in self.__instructors:
            if instructor.disponivel:
                instructor.disponivel = False
                return True
        return False
