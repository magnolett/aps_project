from PySimpleGUI.PySimpleGUI import Print
from tela_login import TelaLogin
from peewee import CharField
from usuario import Usuario



class ControladorLogin():
    def __init__(self):
        self.__tela_login = TelaLogin()

    def abrir_tela_login(self):
        opcao, values = self.__tela_login.abrir()

        continua = True
        logou = False
        while continua and not logou:
            opcao, values = self.__tela_login.abrir()
            if opcao is None or opcao == 0:
                continua = False
            else:
                logou = self.valida_login(values)
        return logou

    def valida_login(self, values):
        login = values['login'].strip()
        senha = values['senha'].strip()
        print('passou')
        print(login)
        print(senha)
        login2, senha2 = self.trazVariavel(login)
        if self.informacoes_suficientes(login, senha):
            if  login2 == login and senha2==senha:
                self.__tela_login.popup(msg='Sucesso')
                return True
            else:
                self.__tela_login.popup(msg='Usuário não encontrado')
                return False
        else:
            self.__tela_login.popup(msg='Informações insuficientes')

    def informacoes_suficientes(self, login, senha):
        if login == '' or login == ' ' or senha == '' or senha == ' ':
            return False
        else:
            return True
    
    # def verificar_usuarios(self, login, senha):
    #     existe, usuario = self.usuario_existe(login, senha)
    #     self.__usuario = usuario
    #     return existe


    # def usuario_existe(self, login, senha):
    #     membro = None
    #     existe = False
    #     if  login2 == login and senha2==senha:
    #         existe = True   
    #     return existe, membro


    def trazVariavel(login):
        print(login)
        senha2 = Usuario.get(Usuario.numero == login).senha
        login2 = Usuario.get(Usuario.numero == login).numero
        return login2, senha2
        
a = ControladorLogin()
a.abrir_tela_login()

