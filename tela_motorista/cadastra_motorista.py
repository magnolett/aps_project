import PySimpleGUI as sg
from abstract_tela import AbstractTela


class TelaCadastraMotorista(AbstractTela):
    def __init__(self):
        super().__init__(nome_tela='tela_cadastra_motorista')

    def init_components(self):
        layout = [
                [sg.Text('Cadastro de motorista', justification='center')],
                [sg.T('*Nome:', size=(24, 1)),
                 sg.In(key='nome')],
                [sg.T('*Senha:', size=(24, 1)),
                 sg.In(key='senha',)],
                [sg.T('*CNH:', size=(24, 1)),
                 sg.In(key='cnh')],
                [sg.T('*Data de Nascimento:', size=(24, 1)),
                 sg.In(key='dtNascimento')],
                [sg.T('*Número de celular:', size=(24, 1)),
                 sg.In(key='numero')],
                [sg.T('*CPF:', size=(24, 1)),
                 sg.In(key='cpf')],
                [sg.T('E-mail:', size=(24, 1)),
                sg.In(key='email')],       
                [sg.T('*Modelo do Veículo:', size=(24, 1)),
                 sg.In(key='modeloVeiculo')],
                [sg.T('*Ano do Veículo:', size=(24, 1)),
                 sg.In(key='anoVeiculo')],
                [sg.Cancel('Cancelar', key=0, size=(10, 1)),
                 sg.Submit('Confirmar', key=1, size=(10, 1))]
                ]

        self.window = sg.Window(self.nome_tela,
                                element_justification='center').Layout(layout)

    def abrir(self):
        button, values = super().abrir()
        return button, values

#a = TelaCadastraMotorista()
#a.abrir()