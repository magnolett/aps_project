from cadastra_motorista import TelaCadastraMotorista
from edita_motorista import TelaEditaMotorista
from motorista import Motorista

# mot1 = Motorista('vini', '123', 'cnh123', '00', '10', '13131', 'Uno', '2010', 'email')
# mot2 = Motorista('matheus', '123', 'cnh321','33', '99', '313131', 'Palio', '2015', 'email2')
# dic_motoristas = {mot1.numero: mot1, mot2.numero: mot2}

cpf = 9390712904

def trazVariavel(cpf, nomeVariavel):
    if nomeVariavel == 'nome':
            return Motorista.get(Motorista.cpf == cpf).nome
    elif nomeVariavel == 'senha':
            return Motorista.get(Motorista.cpf == cpf).senha
    elif nomeVariavel == 'cnh':
            return Motorista.get(Motorista.cpf == cpf).cnh
    elif nomeVariavel == 'dtNascimento':
            return Motorista.get(Motorista.cpf == cpf).dtNascimento
    elif nomeVariavel == 'numero':
            return Motorista.get(Motorista.cpf == cpf).numero
    elif nomeVariavel == 'email':
            return Motorista.get(Motorista.cpf == cpf).email
    elif nomeVariavel == 'modeloVeiculo':
            return Motorista.get(Motorista.cpf == cpf).modeloVeiculo
    elif nomeVariavel == 'anoVeiculo':
            return Motorista.get(Motorista.cpf == cpf).anoVeiculo

b = TelaEditaMotorista(trazVariavel(cpf, 'nome'), trazVariavel(cpf, 'senha'), trazVariavel(cpf, 'numero'), 
trazVariavel(cpf, 'email'), trazVariavel(cpf, 'modeloVeiculo'), trazVariavel(cpf, 'anoVeiculo'))

botoes, values = b.abrir()

if botoes == 0:
    print('encerrando')
else:
    nome = values['nome']
    senha = values['senha']
    numero = values['numero']
    email = values['email']
    modeloVeiculo = values['modeloVeiculo']
    anoVeiculo = values['anoVeiculo']
    deu_certo = True

if nome == '' or senha == '' or numero == '' or modeloVeiculo == '' or anoVeiculo == '':
    print('Preencha todos os dados obrigatórios')
    deu_certo = False
if anoVeiculo < '2010':
    print('Ano do veículo inferior ao mínimo (2010). Sua solicitação foi recusada.')
    deu_certo = False

if deu_certo:
    motoristaEditado = Motorista.update(nome = nome, senha = senha, numero = numero, email = email, modeloVeiculo = modeloVeiculo, anoVeiculo = anoVeiculo)
    motoristaEditado.execute()
# if deu_certo:
#     try:
#         comparaNumero = Motorista.get(Motorista.numero == numero)
#     except Exception:
#         print("Número de telefone não registrado, prosseguindo...")
#         Motorista.insert({
#             Motorista.nome:nome,
#             Motorista.senha:senha,
#             Motorista.numero:numero,
#             Motorista.email:email,
#             Motorista.modeloVeiculo:modeloVeiculo,
#             Motorista.anoVeiculo:anoVeiculo
#         }).execute()
#     else:
#        print('Número já cadastrado no banco de dados.')
# for motorista in dic_motoristas.values():
#     if  motorista.numero == numero and motorista.numero != mot_antes.numero:
#         print('numero repetido')
#         deu_certo = False
# if deu_certo == True:
#     dic_motoristas.update({numero: Motorista(nome, senha, mot_antes.cnh, mot_antes.dtNascimento, numero, mot_antes.cpf, modeloVeiculo, anoVeiculo, email)})
#     mot_depois = dic_motoristas[numero]
#     print(mot_depois.nome, mot_depois.senha, mot_depois.cnh, mot_depois.dtNascimento, mot_depois.numero, mot_depois.email, mot_depois.modeloVeiculo, mot_depois.anoVeiculo)

    