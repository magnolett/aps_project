class Passageiro():
    def __init__(self, nome, senha, data, numero, cpf, email = '', ativo = True):
        self.nome = nome
        self.senha = senha
        self.data = data
        self.numero = numero
        self.cpf = cpf
        self.email = email
        self.ativo = ativo
