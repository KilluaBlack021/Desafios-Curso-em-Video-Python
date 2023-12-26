# programa que le nome, sexo e idade de varias pessoas,
# guardando os dados de cada pessoa em um dicionario e todos eles em uma lista. Por fim, mostre
# quantas pessoas foram cadastradas
# a media de idade do grupo
# uma lista com todas as mulheres
# uma lista com as pessoas com idade acima da média.

pessoas = list()

while True:
    print('-' * 40)
    nome = str(input('NOME: ')).strip()
    print('-' * 40)
    while True:
        sexo = str(input('SEXO [M/F]: ')).strip().upper()
        if sexo[0] not in "MF":
            print('-' * 40)
            print('\033[31mNão entendi!!!\033[m')
        else:
            break
    print('-'*40)
    idade = int(input('IDADE: '))
    print('-' * 40)

    cadastro = {
        'nome': nome,
        'sexo': sexo[0],
        'idade': idade
    }

    pessoas.append(cadastro.copy())

    while True:
        r = str(input('Quer continuar [S/N]: ')).strip().upper()
        if r[0] not in "SN":
            print('-' * 40)
            print('\033[31mNão entendi!!!\033[m')
        else:
            break
    if r == 'N':
        break
print('='*40)

print(f'\n\n{" BANCO DE DADOS ":=^40}', 'só que não kk')
for coisas in range(len(pessoas)):
    print(f'{coisas+1}º pessoa:\n')
    print(f'    {"- NOME ":<10} {pessoas[coisas]["nome"]}')
    print(f'    {"- SEXO ":<10} {pessoas[coisas]["sexo"]}')
    print(f'    {"- IDADE ":<10} {pessoas[coisas]["idade"]}\n\n')
print('='*40)

# Nº cadastros
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('-'*40)

# media de idade
soma = 0
for p in range(len(pessoas)):
    soma += pessoas[p]['idade']
print(f'A média de idade é: {int(soma / len(pessoas))}')
print('-'*40)

# as mulheres
mulheres = list()
for m in range(len(pessoas)):
    if pessoas[m]['sexo'] == 'F':
        mulheres.append(pessoas[m]['nome'])
        if len(mulheres) == 1:
            print('Listagem de mulheres:\n')
        print(f'    - {pessoas[m]["nome"]}')
if len(mulheres) > 0:
    print('-'*40)

# pessoas acima da média de idade
idosos = list()
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > soma / len(pessoas):
        idosos.append(pessoas[i]['nome'])
        if len(idosos) == 1:
            print('Listagem de pessoas com idade acima da média:\n')
        print(f'    - {pessoas[i]["nome"]}')
if len(idosos) != 0:
    print('-'*40)

# eu poderia deixa-lo umas 25 linhas menor facilmente, não o fiz pois queria organiza-lo por "tarefas", criando blocos
