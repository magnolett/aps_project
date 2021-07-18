from cadastra_passageiro import TelaCadastraPassageiro
from edita_passageiro import TelaEditaPassageiro
from passageiro import Passageiro

pass1 = Passageiro('vini', '123', '00', '10','email')
pass2 = Passageiro('matheus', '123', '33', '99', 'email2')
dic_passageiros = {pass1.numero: pass1, pass2.numero: pass2}

pass_antes = dic_passageiros['99']
print(pass_antes.nome)
b = TelaEditaPassageiro(pass2)
botoes, values = b.abrir()
if botoes == 0:
    print('encerrando')
else:
    nome = values['nome']
    senha = values['senha']
    data = values['data']
    numero = values['numero']
    email = values['email']
    cpf = values['cpf']
    deu_certo = True

if nome == '' or senha == '' or data == '' or numero == '' or cpf == '':
    print('preencha todos os dados obrigatórios')
    deu_certo = False
for passageiros in dic_passageiros.values():
    if  passageiros.numero == numero or passageiros.cpf == cpf:
        print('numero ou cpf repetido')
        deu_certo = False
if deu_certo == True:
    dic_passageiros.update({numero: Passageiro(nome, senha, data, numero, email)})
    pass_depois = dic_passageiros[99]
    print(pass_depois.nome, pass_depois.senha, pass_depois.data, pass_depois.numero, pass_depois.email)