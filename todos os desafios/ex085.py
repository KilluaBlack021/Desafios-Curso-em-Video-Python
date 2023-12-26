# usuario digita 7 valores, e o programa os coloca em uma lista, dps
# mostra os números pares e os impares separados, e em ordem crescente

numeros = [[], []]

for c in range(7):
    n = int(input(f'{c+1}º número inteiro: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'\nVocê digitou os seguintes números PARES: {sorted(numeros[0])}')
print(f'\nVocê digitou os seguintes números PARES: {sorted(numeros[1])}')

# print('\nVocê digitou os seguintes números PARES: ', end='')
# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         print(numeros[i], end=' ')
# print('\nVocê digitou os seguintes números IMPARES: ', end='')
# for i in range(len(numeros)):
#     if numeros[i] % 2 != 0:
#         print(numeros[i], end=' ')
