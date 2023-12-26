# programa que lê diversos números e cria uma lista, dps cria outras duas, uma só com par e outra só com número impar

numeros = []
impar = []
par = []

print('='*45)
while True:
    n = int(input('Escreva um número: '))
    numeros.append(n)
    # continua isso ai?
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continua not in 'SN':
        continua = str(input('Tendi isso ai não!!! Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break

# analise
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print('='*45)
print(f'Numeroses: {numeros}')
print(f'Numeros impares: {impar}')
print(f'Numeros pares: {par}')
print('='*45)
