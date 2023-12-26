# programa que tem uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# a primeira função vai sortear 5 números e vai colocá-los dentro de uma lista
# a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ')
    for c in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(.25)
    print('PRONTO!!!')


def soma_par(lista):
    soma = 0
    for coisa in lista:
        if coisa % 2 == 0:
            soma += coisa
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
soma_par(numeros)
