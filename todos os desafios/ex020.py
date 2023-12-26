# este programa sorteiará uma uma sequencia pessoas de uma lista

from random import sample


def linha(tipo):
    if tipo == 1:
        print('-'*80)
    else:
        print('-='*40)


# introducao do rolê
linha(2)
print(f'{"XxSORTEADOR DE SEQUENCIA DE NOMESxX":^80}')
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
print('Referente as pessoas digitadas, a sequencia é: ')
sequencia = sample(pessoas, len(pessoas))
for c in range(0, len(sequencia), 1):
    print(f'{c + 1}º ' + sequencia[c])
linha(2)
print('Tchau!!!')
