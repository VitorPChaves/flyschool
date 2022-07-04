import PySimpleGUI as sg

from src.entity import Aluno


class Schedule:
    SEGUNDA = {'matutino': '11', 'vespertino': '12'}
    TERCA = {'matutino': '21', 'vespertino': '22'}
    QUARTA = {'matutino': '31', 'vespertino': '32'}
    QUINTA = {'matutino': '41', 'vespertino': '42'}
    SEXTA = {'matutino': '51', 'vespertino': '52'}

    @staticmethod
    def schedule_window(aluno: Aluno):
        layout = [
            # A ideia aqui no "usuario logado" é conseguir alterar a view com base no controller
            [sg.Text('Aluno: '), sg.Text(str(aluno.cpf))],
            [sg.Text('Turno: '), sg.Text(str(aluno.turno))],
            [sg.Text('Segunda'), sg.Text('Terca'), sg.Text('Quarta'), sg.Text('Quinta'), sg.Text('Sexta')],
            [sg.Button('Matutino', key=Schedule.SEGUNDA['matutino']), sg.Button('Matutino', key=Schedule.TERCA['matutino']), sg.Button('Matutino', key=Schedule.QUARTA['matutino']), sg.Button('Matutino', key=Schedule.QUINTA['matutino']), sg.Button('Matutino', key=Schedule.SEXTA['matutino'])],
            [sg.Button('Vespertino', key=Schedule.SEGUNDA['vespertino']), sg.Button('Vespertino', key=Schedule.TERCA['vespertino']), sg.Button('Vespertino', key=Schedule.QUARTA['vespertino']), sg.Button('Vespertino', key=Schedule.QUINTA['vespertino']), sg.Button('Vespertino', key=Schedule.SEXTA['vespertino'])],]

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