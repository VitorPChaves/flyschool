from src.entity.aula import Aula
from src.entity.day import Day
from src.entity.professor import Professor
from src.entity.turno import Turno


class InstructorController:
    def __init__(self):
        self.__instructors = []
        self.__professor1 = Professor('567.456.789-10', '123', 18, 70, Turno(), True, Day())
        self.__professor2 = Professor('765.456.789-10', '123', 20, 90, Turno(), True, Day())

        self.__instructors.append(self.__professor1)
        self.__instructors.append(self.__professor2)

    def registered_teachers(self):
        return self.__instructors

    def check_teachers(self, day, period):
        for instructor in self.__instructors:
            if instructor.day.days[day][period]:
                instructor.day.days[day][period] = False
                return True
        return False
