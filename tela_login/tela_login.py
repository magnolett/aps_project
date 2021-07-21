import PySimpleGUI as sg
from abstract_tela import AbstractTela


class TelaLogin(AbstractTela):
    def __init__(self):
        super().__init__(nome_tela='tela_login')

    def init_components(self):
        layout = [
                [sg.T(text='Numero de Celular :', justification='left', pad=((15, 5), (20, 5)), size=(15,1)),
                sg.In(key='login', justification='left', pad=((15, 5), (20, 5)), size=(20,1))],

                [sg.T(text='Senha:', justification='left', pad=((15, 5), (5, 25)), size=(10,1)),
                sg.In(key='senha', password_char='*', justification='left', pad=((15, 5), (5,25)), size=(20,1))],

                [sg.Submit('Confirmar', key=1, size=(10, 1)),
                sg.Cancel('Cancelar', key=0, size=(10, 1))]
            ]

        self.window = sg.Window(title=self.nome_tela,
                                element_justification='center').Layout(layout)

    def abrir(self):
        button, values = super().abrir()
        return button, values




