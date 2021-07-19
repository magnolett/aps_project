from cadastra_passageiro import TelaCadastraPassageiro
from edita_passageiro import TelaEditaPassageiro
from passageiro import Passageiro

pass1 = Passageiro('vini', 'senha1', 'data1', 'numero11', '000','email')
pass2 = Passageiro('matheus', '123', '33', '99', '100', 'email2')
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
    numero = values['numero']
    email = values['email']
    deu_certo = True

    if nome == '' or senha == ''  or numero == '' :
        print('preencha todos os dados obrigatórios')
        deu_certo = False
    for passageiros in dic_passageiros.values():
        if  passageiros.numero == numero and passageiros.numero != pass_antes.numero:
            print('numero repetido')
            deu_certo = False
    if deu_certo == True:
        dic_passageiros.update({numero: Passageiro(nome, senha, pass_antes.data, numero, pass_antes.cpf, email)})
        pass_depois = dic_passageiros[numero]
        print(pass_depois.nome, pass_depois.senha, pass_depois.data, pass_depois.numero, pass_depois.cpf, pass_depois.email)