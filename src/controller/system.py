from src.controller.agenda import ScheduleController
from src.controller.login import LoginController


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__schedule_controller = ScheduleController(self)

    def open_login_window(self):
        self.__login_controller.open_window()

    def open_schedule_window(self):
        self.__schedule_controller.open_window()

    def exit(self):
        exit(0)
