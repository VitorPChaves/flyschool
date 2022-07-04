import PySimpleGUI as sg

from src.entity import Aluno


class Schedule:
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 6
    SEXTA = 7

    @staticmethod
    def schedule_window(aluno: Aluno):
        layout = [
            # A ideia aqui no "usuario logado" é conseguir alterar a view com base no controller
            [sg.Text('Aluno: '), sg.Text(str(aluno.cpf))],
            [sg.Text('Turno: '), sg.Text(str(aluno.turno))],
            [sg.Text('Segunda'), sg.Text('Terca'), sg.Text('Quarta'), sg.Text('Quinta'), sg.Text('Sexta')],
            [sg.Button('VAGA', key=Schedule.SEGUNDA), sg.Button('VAGA', key=Schedule.TERCA), sg.Button('VAGA', key=Schedule.QUARTA), sg.Button('VAGA', key=Schedule.QUINTA), sg.Button('VAGA', key=Schedule.TERCA)],
            [sg.Button('VAGA', key=Schedule.SEGUNDA), sg.Button('VAGA', key=Schedule.TERCA), sg.Button('VAGA', key=Schedule.QUARTA), sg.Button('VAGA', key=Schedule.QUINTA), sg.Button('VAGA', key=Schedule.TERCA)],
            [sg.Button('VAGA', key=Schedule.SEGUNDA), sg.Button('VAGA', key=Schedule.TERCA), sg.Button('VAGA', key=Schedule.QUARTA), sg.Button('VAGA', key=Schedule.QUINTA), sg.Button('VAGA', key=Schedule.TERCA)],
            [sg.Button('VAGA', key=Schedule.SEGUNDA), sg.Button('VAGA', key=Schedule.TERCA), sg.Button('VAGA', key=Schedule.QUARTA), sg.Button('VAGA', key=Schedule.QUINTA), sg.Button('VAGA', key=Schedule.TERCA)],
            [sg.Button('VAGA', key=Schedule.SEGUNDA), sg.Button('VAGA', key=Schedule.TERCA), sg.Button('VAGA', key=Schedule.QUARTA), sg.Button('VAGA', key=Schedule.QUINTA), sg.Button('VAGA', key=Schedule.TERCA)],
        ]

        window = sg.Window('FlySchool Agenda', layout=layout, finalize=True, resizable=True, element_justification='c')
        button, values = window.read()
        window.close()

        # Imagino que tenha que retornar a window também pra conseguir dar window[Schedule.SEGUNDA].Update(str(aluno.nome))
        return {'action': button}

    """
    def read_schedule_window(self):
        window = self.schedule_window()
        try:
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == 'VAGA':
                    self.__agenda.choose_class()

        except Exception as e:
            sg.popup_error_with_traceback('Erro', e)

        return {'action': event, 'user': values}
    """

    def confirmation_window(self):
        return

    @staticmethod
    def notify(mensagem: str):
        sg.popup_ok(mensagem)