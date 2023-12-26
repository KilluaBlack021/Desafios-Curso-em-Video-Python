# programa que le um numero inteiro calcula os n primeiros numeros de uma sequencia de Fibonacci


ultimo = penultimo = 1
numeros_sequencia = int(input('Escreva quantos números da sequencia de Fibonacci você quer saber: '))


print('SEQUÊNCIA: ', end=' ')
if numeros_sequencia == 1:
    print("1")
else:
    print('1 1', end=' ')
    while numeros_sequencia != 2:
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
        print(atual, end=' ')
        numeros_sequencia -= 1
