from src.view.login import Login

from src.controller.aluno import StudentController


class LoginController:

    def __init__(self, system_controller):
        self.__login_window = Login()
        self.__aluno = StudentController()
        self.__system = system_controller

    # Checar se é Aluno, Instrutor ou Coordenador
    def authentication(self, cpf, senha):
        alunos = self.__aluno.registered_students()

        for aluno in alunos:
            if aluno.cpf == cpf and aluno.senha == senha:
                # open schedule
                self.__system.open_schedule_window()
            else:
                self.__login_window.notify('Dados incorretos!')

    def open_window(self):
        try:
            window_navigation_options = {
                None: self.__system.exit,
                Login.LOGIN: self.authentication
            }
            while True:
                options = self.__login_window.login_window()
                selected_option = window_navigation_options[options['action']]
                selected_option(cpf=options['user']['cpf'], senha=options['user']['senha'])
        except Exception as e:
            self.__login_window.notify(str(e))
