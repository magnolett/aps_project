from cadastra_motorista import TelaCadastraMotorista
from motorista import Motorista

# mot1 = Motorista('vini', '123', 'cnh321', '00', '10', '000','email', 'Gol', '2009')
#mot2 = Motorista('matheus', '123', 'cnh123', '33', '99', '100', 'email2', 'Siena', '2020')
#dic_motorista = {mot1.numero: mot1, mot2.numero: mot2}

a = TelaCadastraMotorista()
botoes, values = a.abrir()
nome = values['nome'] 
senha = values['senha']
cnh = values['cnh']
dtNascimento = values['dtNascimento']
numero = values['numero']
email = values['email']
cpf = values['cpf']
modeloVeiculo = values['modeloVeiculo']
anoVeiculo = values['anoVeiculo']

deu_certo = True

def validaString(valor):
    return any(chr.isdigit() for chr in valor)

if nome == '' or senha == '' or cnh == '' or dtNascimento == '' or numero == '' or cpf == '' or modeloVeiculo == '' or anoVeiculo == '':
    print('Preencha todos os dados obrigatórios')
    deu_certo = False

if validaString(nome) or validaString(modeloVeiculo):
    print('Oops... Somente letras são válidas para NOME e MODELO DO VEÍCULO!')
    deu_certo = False

if not validaString(cnh) or not validaString(numero) or not validaString(cpf) or not validaString(anoVeiculo):
    print('Oops.. para os campos CNH, NÚMERO, CPF e ANO VEÍCULO, somente números são permitidos!')
    deu_certo = False

elif len(cpf) != 11 and len(numero) != 9:
    print('CPF precisa ter EXATOS 11 dígitos e o número de celular precisa ter EXATOS 9 dígitos!')
    deu_certo = False

elif anoVeiculo < '2010':
    print('Ano do veículo inferior ao mínimo (2010). Sua solicitação foi recusada.')
    deu_certo = False

if deu_certo:
    try:
        compara = Motorista.get(Motorista.cpf == cpf)
    except Exception:
        print("CPF não registrado, prosseguindo...")
        try :
            comparaNumero = Motorista.get(Motorista.numero == numero)
        except Exception:
            print("Número de telefone não registrado, prosseguindo...")
            try:
                comparaCnh = Motorista.get(Motorista.cnh == cnh)
            except Exception:
                print("CNH não encontrada, prosseguindo...")
                Motorista.insert({
                    Motorista.nome:nome,
                    Motorista.senha:senha,
                    Motorista.cnh:cnh,
                    Motorista.dtNascimento:dtNascimento,
                    Motorista.numero:numero,
                    Motorista.email:email,
                    Motorista.cpf:cpf,
                    Motorista.modeloVeiculo:modeloVeiculo,
                    Motorista.anoVeiculo:anoVeiculo
                }).execute()
            else:
                print("CNH já cadastrada no banco de dados.")
        else:
            print('Número já cadastrado no banco de dados.')

    else:
        print('CPF já existente no banco de dados.')

    #  Motorista.create(nome, senha, cnh, dtNascimento, numero, email, cpf, modeloVeiculo, anoVeiculo)

    # Motorista.create(novo_motorista)
    
    # Motorista.nome = nome
    # Motorista.senha = senha
    # Motorista.cnh = cnh
    # Motorista.dtNascimento = dtNascimento
    # Motorista.numero = numero
    # Motorista.email = email
    # Motorista.cpf = cpf
    # Motorista.modeloVeiculo = modeloVeiculo
    # Motorista.anoVeiculo = anoVeiculo
