# programa que le nome e peso de varias pessoas, e guarda numa lista. No fim, mostra:
# n pessoas cadastradas
# pessoas mais pesadas
# pessoas mais leves

pessoas = []
# contador = 0

# perfumaria
print('='*40)
print(f'{" CADASTRO DE PESSOAS ":-^40}')
print('='*40)

# main
while True:
    pessoa = []
    nome = str(input('NOME: ')).strip()
    peso = float(input('PESO: '))
    # contador += 1

    pessoa.append(nome)
    pessoa.append(peso)

    pessoas.append(pessoa[:])

    print('-'*40)
    r = str(input('Quer add mais alguem? [S/N] ')).strip().upper()
    while r not in "SN":
        r = str(input('Não entendi!!!\nQuer add mais alguem? [S/N] ')).strip().upper()
    print('-' * 40)
    if r == "N":
        break


# mostrando as coisas

# tabela
print('='*40)
print(f'\n\n{" PESSOAS ":=^40}')
for i in range(len(pessoas)):
    print(f"{pessoas[i][0]:.<30}" + f"{pessoas[i][1]:.>8}Kg")
print('='*40, '\n')

# Nº pessoas cadastradas
print(f'Nº de pessoas cadastradas: {len(pessoas)}')

# Pessoas mais pesadas e mais leves
copia_pessoas = sorted(pessoas, key=lambda x: x[1])

if len(copia_pessoas) >= 2:
    print(f'\n{" PESSOAS MAIS PESADAS ":-^40}')
    for c in range(0, 2):
        print(f'{str(copia_pessoas[-c - 1][0]):>18} | {str(copia_pessoas[-c - 1][1]):<18}')
    print('-'*40)

    print(f'\n{" PESSOAS MAIS LEVES ":-^40}')
    for c in range(0, 2):
        print(f'{str(copia_pessoas[c][0]):>18} | {str(copia_pessoas[c][1]):<18}')
    print('-' * 40)

"""NÃO GOSTEI DESSE MÉTODO, APESAR DO TRABALHÃO QUE DEU

# Pessoas mais pesadas
copia_pessoas = pessoas[:]
print('Pessoas mais pesadas foram: ', end=' ')
for count in range(2):
    maiores.append(max(copia_pessoas))
    print(max(copia_pessoas), end=' ')
    coordenada_max = copia_pessoas.index(max(copia_pessoas))
    copia_pessoas.remove(max(copia_pessoas))

# Pessoas mais leves
copia_pessoas = pessoas[:]
print('\nPessoas mais leves foram: ', end=' ')
for count in range(2):
    menores.append(min(copia_pessoas))
    print(min(copia_pessoas), end=' ')
    coordenada_max = copia_pessoas.index(min(copia_pessoas))
    copia_pessoas.remove(min(copia_pessoas))"""
