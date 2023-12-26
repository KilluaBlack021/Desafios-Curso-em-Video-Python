# programa que leia um número inteiro e diz se ele é primo

numero = int(input('Escreva um número inteiro: '))
contador = 0

for c in range(1, numero):
    if numero % c == 0:
        contador += 1

if contador == 1:
    print(f'O numero {numero}, É PRIMO!')
else:
    print(f'O número {numero}, NÃO É PRIMO!')

print('Tchau!!!')
