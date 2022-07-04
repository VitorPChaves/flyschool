from src.view.schedule import Schedule

from src.entity.aluno import Aluno
from src.entity.aula import Aula
from src.controller.professor import InstructorController
from src.controller.paraquedas import ParachuteController


class ScheduleController:

    def __init__(self, system_controller):
        self.__schedule_window = Schedule()
        #self.__class = Aula()
        self.__instructor_controller = InstructorController()
        self.__parachute_controller = ParachuteController()
        self.__system = system_controller

    # Passar o dia escolhido para agendar corretamente a aula do dia certo
    def choose_class(self, aluno: Aluno):
        self.check_class(aluno)

    def check_class(self, aluno: Aluno):
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
    # Colocar o nome do aluno no lugar do botão VAGA
    # Abrir popup de confirmação da aula
    def confirm_class(self, aluno: Aluno):
        self.__schedule_window.notify('Aula marcada!')
        print(aluno.cpf)

    def open_window(self):
        try:
            action_options = {
                None: self.__system.exit,
                1: self.choose_class,

            }
            # Definir as ações para a aula selecionada
            while True:
                logged_user = self.__system.logged_user
                option_number = self.__schedule_window.schedule_window(logged_user)
                selected_function = action_options[option_number]
                selected_function()
                print(self.__system.__logged_user)
        except Exception as e:
            self.__schedule_window.notify(str(e))

    # Mudar o texto do botão para o nome do aluno
    def change_button_text(self):
        return 0


