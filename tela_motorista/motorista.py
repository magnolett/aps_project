from peewee import DateField, IntegerField, Model, TextField
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('db_aps', host='localhost', port=3306, user='root', password='root')


class Motorista(Model):

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
    dtNascimento=DateField()
    numero=IntegerField()
    cpf=IntegerField(primary_key=True)
    email=TextField()
    modeloVeiculo=TextField()
    anoVeiculo=IntegerField()
    
    class Meta:
        database=db
        db_table='Motorista'

db.connect
db.create_tables([Motorista])

