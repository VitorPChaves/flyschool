import PySimpleGUI as sg

import src.controller.login

from src.view.schedule import Schedule


class Login:
    LOGIN = 1

    @staticmethod
    def login_window():
        layout = [
            [sg.Text('CPF')],
            [sg.InputText(size=(30, 1), key='cpf')],
            [sg.Text('SENHA')],
            [sg.InputText(size=(30, 1), key='senha',  password_char='*')],
            [sg.Button('Entrar', key=Login.LOGIN)],
        ]
        window = sg.Window('FlySchool Login', layout=layout, finalize=True, resizable=True, element_justification='c')
        event, values = window.read()

        window.close()

        # Retorna um array com a opção clicada e quem clicou
        return {'action': event, 'user': values}

    """
    def read_login_window(self):
        window = self.login_window()

        try:
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == 'Entrar':
                    self.__login.authentication(values['cpf'], values['senha'])

        except Exception as e:
            sg.popup_error_with_traceback('Erro', e)
    """

    @staticmethod
    def notify(mensagem: str):
        sg.popup_ok(mensagem)
