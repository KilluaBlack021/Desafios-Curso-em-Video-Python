# programa que gerará 5 numeros aleatórios e os colocara em uma tupla. Depois
# mostra a listagem dos numeros e diz o menor e o maior valor

from random import randint

n_max = 10
#maior = menor = 0
numeros = (randint(0, n_max), randint(0, n_max), randint(0, n_max), randint(0, n_max), randint(0, n_max))

print('Numeros sorteados: ', end='')
for i in range(len(numeros)):
    print(numeros[i], end=' ')
    # if i == 0:
    #     maior = numeros[i]
    #     menor = numeros[i]
    # else:
    #     maior = numeros[i] if numeros[i] > maior else maior
    #     menor = numeros[i] if numeros[i] < menor else menor


print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
