# programa que sorteia o nome de uma pessoa

from random import choice


def linha(tipo):
    if tipo == 1:
        print('-'*80)
    else:
        print('-='*40)


# introducao do rolê
linha(2)
print(f'{"XxSORTEADOR DE NOMESxX":^80}')
linha(2)

# principal
pessoas = [str(input('Escreva um nome: '))]
while True:
    pessoa = str(input('Escreva outro nome: '))
    pessoas.append(pessoa)
    print('-'*80)
    q = str(input('Quer adicionar mais alguem? Aperte apenas "Enter", se não aperte outra coisa: '))
    linha(1)
    if q != " " and q != "":
        break
    else:
        continue

linha(2)
print(f'Referente as pessoas digitadas, a escolhida foi "{choice(pessoas)}"')
linha(2)
print('Tchau!!!')
