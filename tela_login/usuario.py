from peewee import BigIntegerField, BooleanField, DateField, IntegerField, Model, TextField
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('db_aps', host='localhost', port=3306, user='root', password='root')


class Usuario(Model):

    # def __init__(self, nome, senha, cnh, dtNascimento, numero, cpf, modeloVeiculo, anoVeiculo, email = ''):
    #     self.nome = nome
    #     self.senha = senha
    #     self.cnh = cnh
    #     self.dtNascimento = dtNascimento
    #     self.numero = numero
    #     self.cpf = cpf
    #     self.email = email
    #     self.modeloVeiculo = modeloVeiculo
    #     self.anoVeiculo = anoVeiculo

    nome=TextField()
    senha=TextField()
    cnh=TextField()
    dtNascimento=TextField()
    numero=TextField()
    cpf=BigIntegerField(primary_key=True)
    email=TextField(default=True)
    ativo=BooleanField()
    modeloVeiculo=TextField()
    anoVeiculo=IntegerField()
    
    class Meta:
        database=db
        db_table='Usuario'

db.connect
db.create_tables([Usuario])

