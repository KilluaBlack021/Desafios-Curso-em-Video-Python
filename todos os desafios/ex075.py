# programa que le 4 valores pelo teclado e põe numa tupla. No final
# quantas vezes apareceu o valor 9
# em que posição foi digitado o valor 3
# quais números são pares

print('='*45)
numeros = (int(input(f'Escreva o 1º numero: ')), int(input(f'Escreva o 2º numero: ')),
           int(input(f'Escreva o 3º numero: ')), int(input(f'Escreva o 4º numero: ')))
print('='*45)

print(f'Há {numeros.count(9)} numeros 9.')
if 3 in numeros:
    print(f'A posição do numero 3 é {numeros.index(3) + 1}')
print('Números pares digitados foram: ', end='')

c = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')
        c += 1
if c == 0:
    print('"NÃO HOUVE NÚMEROS PARES"')
