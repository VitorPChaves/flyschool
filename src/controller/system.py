from src.controller.agenda import ScheduleController
from src.controller.login import LoginController
from src.controller.paraquedas import ParachuteController
from src.controller.professor import InstructorController


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__schedule_controller = ScheduleController(self)
        self.__parachute_controller = ParachuteController(self)
        self.__instructor_controller = InstructorController(self)

    def open_login_window(self):
        self.__login_controller.open_window()

    def open_schedule_window(self):
        self.__schedule_controller.open_window()

    def exit(self):
        exit(0)
