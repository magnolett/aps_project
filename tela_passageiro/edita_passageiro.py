import PySimpleGUI as sg
from abstract_tela import AbstractTela


class TelaEditaPassageiro(AbstractTela):
    def __init__(self, nome, senha, numero, email):
        super().__init__(nome_tela='tela_edita_passageiro')
        self.nome = nome
        self.senha = senha
        self.numero = numero
        self.email = email

    def init_components(self):
        layout = [
                [sg.Text('Cadastro de passageiro', justification='center')],
                [sg.T('Nome:', size=(24, 1)),
                 sg.In(key='nome', default_text=self.nome)],
                [sg.T('Senha:', size=(24, 1)),
                 sg.In(key='senha', default_text=self.senha)],
                [sg.T('Número de celular:', size=(24, 1)),
                 sg.In(key='numero', default_text=self.numero)],
                [sg.T('E-mail:', size=(24, 1)),
                 sg.In(key='email', default_text=self.email)],
                [sg.Cancel('Cancelar', key=0, size=(10, 1)),
                 sg.Submit('Confirmar', key=1, size=(10, 1))]
                ]

        self.window = sg.Window(self.nome_tela,
                                element_justification='center').Layout(layout)

    def abrir(self):
        button, values = super().abrir()
        return button, values

#a = TelaEditaPassageiro(1)
#a.abrir()