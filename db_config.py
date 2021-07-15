import pymysql
from pessoa import Pessoa
from playhouse.mysql_ext import MySQLConnectorDatabase
from peewee import BooleanField, IntegerField, Model, MySQLDatabase, TextField
#from pessoa import Pessoa

db = MySQLConnectorDatabase('db_aps', host='localhost', port=3306, user='root', password='root')
#db = MySQLDatabase('db_aps', host='localhost', port=3306, user='root', password='root')

class Passageiro(Model):
    name=TextField
    cpf=IntegerField
    ativo=BooleanField

    def __init__(self, nome, cpf, ativo:bool):
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
    
    class Meta:
        database=db
        db_table='Passageiro'



db.connect()
db.create_tables([Passageiro])

