from cadastra_passageiro import TelaCadastraPassageiro
from edita_passageiro import TelaEditaPassageiro
from passageiro import Passageiro

# pass1 = Passageiro('vini', 'senha1', 'data1', '123456789', '00000000000','email')
#pass2 = Passageiro('matheus', '123', '33', '999999999', '12345678901', 'email2')
# dic_passageiros = {pass1.numero: pass1, pass2.numero: pass2}
#pass_antes = dic_passageiros['123456789']
#print(pass_antes.nome)
numero_do_passageiro = '111111112'
try:
    pnumero = Passageiro.get(Passageiro.numero == numero_do_passageiro).numero
    pnome = Passageiro.get(Passageiro.numero == numero_do_passageiro).nome
    psenha = Passageiro.get(Passageiro.numero == numero_do_passageiro).senha
    pemail = Passageiro.get(Passageiro.numero == numero_do_passageiro).email
except:
    'nao foi possivel achar os dados'
print(pnumero, pnome)

b = TelaEditaPassageiro(pnome,psenha, pnumero, pemail)
botoes, values = b.abrir()
if botoes == 0:
    print('encerrando')
elif botoes == None:
    print('encerrando')
else:
    nome = values['nome']
    senha = values['senha']
    numero = values['numero']
    email = values['email']
    deu_certo = True

    if nome == '' or senha == ''  or numero == '':
        print('preencha todos os dados obrigatórios')
        deu_certo = False
    elif len(numero) != 9:
        print('verifique os campos CPF e numero de celular')
        deu_certo = False
    else:
        try: 
            int(numero)
        except:
            print('CPF e Numero de celular devem conter apenas numero')
            deu_certo = False


    if deu_certo:
                atualizar = Passageiro.update(nome = nome, senha = senha, numero = numero, email =  email).where(Passageiro.numero == numero_do_passageiro)
                atualizar.execute()
    # for passageiros in dic_passageiros.values():
    #     if  passageiros.numero == numero and passageiros.numero != pass_antes.numero:
    #         print('esse numero ja foi usado')
    #         deu_certo = False
    # if deu_certo == True:
    #     dic_passageiros.update({numero: Passageiro(nome, senha, pass_antes.data, numero, pass_antes.cpf, email)})
    #     pass_depois = dic_passageiros[numero]
    #     print(pass_depois.nome, pass_depois.senha, pass_depois.data, pass_depois.numero, pass_depois.cpf, pass_depois.email)