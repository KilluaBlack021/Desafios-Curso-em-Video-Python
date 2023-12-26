# programa que le 5 valores numericos e guarda em uma lista. No final
# mostra qual foi o maior e o menor valor digitado e suas posições na lista


numeros = []
maior = 0
menor = 0

print('='*45)
for c in range(5):
    n = int(input(f'Escreva {c+1}º numero de uma lista: '))
    numeros.append(n)
print('='*45)

# números digitados
print(f'os números digitados foram: ')
for c in range(len(numeros)):
    print(f'{c}º  {numeros[c]}')

# maior número e onde ele foi encontrado
print(f'\nO maior número digitado foi: {max(numeros)}, encontrado na(s) posição(ções): ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(i, end=' ')

# menor número e onde ele foi encontrado
print(f'\nO menor número digitado foi: {min(numeros)}, encontrado na(s) posição(ções): ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(i, end=' ')
