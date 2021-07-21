from cadastra_passageiro import TelaCadastraPassageiro
from edita_passageiro import TelaEditaPassageiro
from passageiro import Passageiro
from datetime import date, timedelta

#pass1 = Passageiro('vini', '123', '00', '123456789', '000','email')
#pass2 = Passageiro('matheus', '123', '33', '99', '100', 'email2')
#dic_passageiros = {pass1.numero: pass1, pass2.numero: pass2}

a = TelaCadastraPassageiro()
botoes, values = a.abrir()
nome = values['nome'] 
senha = values['senha']
data = values['data']
numero = values['numero']
email = values['email']
cpf = values['cpf']
#print('nome = ',nome, senha)
deu_certo = True

if botoes == 0:
    print('encerrando')
elif botoes == None:
    print('encerrando')

else:
    if nome == '' or senha == '' or data == '' or numero == '' or cpf == '':
        print('preencha todos os dados obrigatórios')
        deu_certo = False
    elif len(cpf) != 11 and len(numero) != 9:
        print('verifique os campos CPF e numero de celular')
        deu_certo = False
    
    else:
        try: 
            int(cpf) and int(numero)
        except:
            print('CPF e Numero de celular devem conter apenas numero')
            deu_certo = False
    
    

    if deu_certo :
        try:
            compara= Passageiro.get(Passageiro.cpf == cpf)
            print('aa', compara)
        except Exception:
            try :
                comparaNumero = Passageiro.get(Passageiro.numero == numero)
            except Exception:
                    Passageiro.insert({
                    Passageiro.nome:nome,
                    Passageiro.senha:senha,
                    Passageiro.dtNascimento:data,
                    Passageiro.numero:numero,
                    Passageiro.email:email,
                    Passageiro.cpf:cpf,
                }).execute()
            else:
                print('Número já cadastrado no banco de dados.')

        else:
            print('CPF já existente no banco de dados.')
    
    #for passageiros in dic_passageiros.values():
    #if  passageiros.numero == numero or passageiros.cpf == cpf:
    #    print('numero ou cpf repetido')
    #    deu_certo = False
    # if deu_certo == True:
    #     Passageiro.get_
    #     novo_passageiro = Passageiro(values['nome'], values['senha'], values['data'], values['numero'], values['email'], values['cpf'])
    #     dic_passageiros[values['numero']] = novo_passageiro
    #     print(dic_passageiros)
