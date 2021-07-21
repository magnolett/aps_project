from playhouse.mysql_ext import MySQLConnectorDatabase
from peewee import BooleanField, IntegerField, Model, TextField

db = MySQLConnectorDatabase('db_aps', host='localhost', port=3306, user='root', password='root')
#db = MySQLDatabase('db_aps', host='localhost', port=3306, user='root', password='root')

class Usuarios(Model):
    name=TextField
    cpf=IntegerField(primary_key=True)
    ativo=BooleanField
    senha=TextField

    def __init__(self, nome, cpf, ativo:bool, senha):
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
        self.senha = senha
    
    class Meta:
        database=db
        db_table='Usuarios'



db.connect()
db.create_tables([Usuarios])

