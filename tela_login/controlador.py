from tela_login import TelaLogin
from peewee import CharField



class ControladorLogin:
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
        if self.informacoes_suficientes(login, senha):
            if self.verificar_usuarios(login, senha):
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
    
    def verificar_usuarios(self, login, senha):
        existe, usuario = self.usuario_existe(login, senha)
        self.__usuario = usuario
        return existe

    
    def usuario_existe(self, login, senha):
        membro = None
        existe = False
        try:
            login = int(login)
            membro = self.__membros_dao.get(login)
            existe = membro.compara_senha(senha)
        except AttributeError:
            pass
        except ValueError:
           pass 
        return existe, membro


a = ControladorLogin()
a.abrir_tela_login()