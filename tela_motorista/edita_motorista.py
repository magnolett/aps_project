from sys import modules 
import PySimpleGUI as sg
from abstract_tela import AbstractTela


class TelaEditaMotorista(AbstractTela):
    def __init__(self, motorista):
        super().__init__(nome_tela='tela_edita_motorista')
        self.motorista = motorista

    def init_components(self):
        layout = [
                [sg.Text('Editar motorista', justification='center')],
                [sg.T('Nome:', size=(24, 1)),
                 sg.In(key='nome', default_text=self.motorista.nome)],
                [sg.T('Senha:', size=(24, 1)),
                 sg.In(key='senha', default_text=self.motorista.senha)],
                [sg.T('Número de celular:', size=(24, 1)),
                 sg.In(key='numero', default_text=self.motorista.numero)],
                [sg.T('E-mail:', size=(24, 1)),
                 sg.In(key='email', default_text=self.motorista.email)],
                [sg.T('Modelo do Veículo:', size=(24, 1)),
                 sg.In(key='modeloVeiculo', default_text=self.motorista.modeloVeiculo)],
                [sg.T('Ano do Veículo:', size=(24, 1)),
                 sg.In(key='anoVeiculo', default_text=self.motorista.anoVeiculo)],
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