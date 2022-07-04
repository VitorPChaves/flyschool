from src.entity import Aluno
from src.view.login import Login

from src.controller.aluno import StudentController


class LoginController:

    def __init__(self, system_controller):
        self.__login_window = Login()
        self.__aluno = StudentController()
        self.__system = system_controller

    def save_user(self, aluno: Aluno):
        self.__system.set_logged_user(aluno)

    # Checar se é Aluno, Instrutor ou Coordenador
    def authentication(self, cpf, senha):
        alunos = self.__aluno.registered_students()

        for aluno in alunos:
            if aluno.cpf == cpf and aluno.senha == senha:
                # open schedule
                self.save_user(aluno)
                self.__system.open_schedule_window()
                print(aluno.cpf)
            else:
                self.__login_window.notify('Dados incorretos!')

    def open_window(self):
        try:
            window_options = {
                None: self.__system.exit,
                Login.LOGIN: self.authentication
            }
            while True:
                options = self.__login_window.login_window()
                selected_option = window_options[options['action']]
                selected_option(cpf=options['user']['cpf'], senha=options['user']['senha'])
        except Exception as e:
            e = 'Obrigado, volte sempre!'
            self.__login_window.notify(str(e))
