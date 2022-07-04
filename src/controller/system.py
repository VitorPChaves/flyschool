from src.controller.agenda import ScheduleController
from src.controller.login import LoginController
from src.entity import Usuario, Aluno


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__schedule_controller = ScheduleController(self)
        self.__logged_user: Aluno or None = None

    @property
    def logged_user(self) -> Aluno:
        return self.__logged_user

    def set_logged_user(self, aluno: Aluno):
        self.__logged_user = aluno

    def open_login_window(self):
        self.__login_controller.open_window()

    def open_schedule_window(self):
        self.__schedule_controller.open_window()

    def exit(self):
        exit(0)
