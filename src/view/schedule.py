import PySimpleGUI as sg

from src.controller.agenda import ScheduleController


class Schedule:

    def __init__(self):
        self.__agenda = ScheduleController()

    @staticmethod
    def schedule_window():
        layout = [
            [sg.Text('AGENDA', size=(6, 1))],
            [sg.Button('VAGA')],
            [sg.Button('VAGA')],
            [sg.Button('VAGA')],
            [sg.Button('VAGA')],
        ]

        return sg.Window('FlySchool Agenda', layout=layout, finalize=True)

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

    def confirmation_window(self):
        return

    @staticmethod
    def notify(mensagem: str):
        print(mensagem)
