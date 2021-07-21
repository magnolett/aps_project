from abc import ABC, abstractmethod
from PySimpleGUI import Popup, ChangeLookAndFeel, SetOptions


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, nome_tela):
        self.__window = None
        self.__nome_tela = nome_tela
        ChangeLookAndFeel('DarkGrey11')


    # Properties e Setters

    @property
    def controlador(self):
        return self.__controlador

    @property
    def nome_tela(self):
        return self.__nome_tela

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window


    # Inicialização da tela

    @abstractmethod
    def init_components(self, **kwargs):
        pass

    def abrir(self, **kwargs):
        self.init_components(**kwargs)
        button, values = self.__window.Read()
        self.fechar()
        return button, values

    def fechar(self):
        self.__window.Close()

    @staticmethod
    def popup(titulo: str = 'Alerta', msg: str = ''):
        Popup(msg, title=titulo)
