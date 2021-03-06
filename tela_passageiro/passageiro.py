from peewee import DateField, IntegerField, Model, TextField, BooleanField, BigIntegerField
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('db_aps', host='localhost', port=3306, user='root', password='root')

class Passageiro(Model):
    # def __init__(self, nome, senha, data, numero, cpf, email = '', ativo = True):
    #     self.nome = nome
    #     self.senha = senha
    #     self.data = data
    #     self.numero = numero
    #     self.cpf = cpf
    #     self.email = email
    #     self.ativo = ativo

    nome=TextField()
    senha=TextField()
    dtNascimento=DateField()
    numero=IntegerField()
    cpf=BigIntegerField(primary_key=True)
    email=TextField()
    ativo=BooleanField(default=True)


    class Meta:
        database=db
        db_table='Passageiro'

db.connect
db.create_tables([Passageiro])
