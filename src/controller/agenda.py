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
    def choose_class(self, aluno: Aluno, day, period):
        self.check_class(aluno, day, period)

    def check_class(self, aluno: Aluno, day, period):
        # Já ocupa os paraquedas com base no nivel do aluno
        if not aluno.day.days[day][period]:
            self.__schedule_window.notify('Você já reservou este horário')
        else:
            aluno.day.days[day][period] = False
            available_parachutes = self.__parachute_controller.check_parachutes(aluno, day, period)
            if aluno.nivel.name == 'INICIANTE':
                available_instructor = self.__instructor_controller.check_teachers(day, period)
                if not available_instructor:
                    aluno.day.days[day][period] = True
                    self.__schedule_window.notify('Não há professores disponíveis!')
                else:
                    if not available_parachutes:
                        aluno.day.days[day][period] = True
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
                '1': 'segunda',
                '2': 'terca',
                '3': 'quarta',
                '4': 'quinta',
                '5': 'sexta',

            }
            # Definir as ações para a aula selecionada
            while True:
                logged_user = self.__system.logged_user
                option_number = self.__schedule_window.schedule_window(logged_user)
                selected_function = action_options[option_number['action'][0]]
                if option_number['action'][1] == '1':
                    period = 'matutino'
                else:
                    period = 'vespertino'
                self.choose_class(logged_user, selected_function, period)
        except Exception as e:
            self.__schedule_window.notify(str(e))

    # Mudar o texto do botão para o nome do aluno
    def change_button_text(self):
        return 0


