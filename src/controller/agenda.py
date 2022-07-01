from ..view import schedule

from src.entity.aluno import Aluno
from src.entity.aula import Aula
from src.entity.professor import Professor
from src.entity.paraquedas import Paraquedas

from src.controller.professor import InstructorController
from src.controller.paraquedas import ParachuteController


class ScheduleController:

    def __init__(self, system_controller):
        self.__schedule_window = schedule.Schedule()
        self.__class = Aula()
        self.__instructor_controller = InstructorController()
        self.__parachute_controller = ParachuteController()
        self.__system = system_controller

    def choose_class(self):
        self.check_class()

    def check_class(self, aluno):
        # Já ocupa os paraquedas com base no nivel do aluno
        available_parachutes = self.__parachute_controller.check_parachutes(aluno)

        if aluno == 'INICIANTE':
            available_instructor = self.__instructor_controller.check_teachers()
            if not available_instructor:
                self.__schedule_window.notify('Não há professores disponíveis!')
            else:
                if not available_parachutes:
                    self.__schedule_window.notify('Não há paraquedas disponíveis!')
                else:
                    self.confirm_class(aluno)
        else:
            if not available_parachutes:
                self.__schedule_window.notify('Não há paraquedas disponíveis!')
            else:
                self.confirm_class(aluno)

    # Colocar em ClassController()
    def confirm_class(self, aluno: Aluno):
        # self.__schedule_window.
        self.__schedule_window.notify('Aula marcada!')

    def open_window(self):
        try:
            action_options = {
                None: self.__system.exit,
                MenuBoundary.SHUTDOWN: self.__system_controller.shutdown,
                MenuBoundary.OPEN_PROFILE: self.see_client_profile,
                MenuBoundary.SCHEDULE_SERVICE: self.see_schedule_service_screen
            }
            while True:
                option_number = self.__menu_screen.open_menu_client()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__menu_screen.show_message(str(e))


