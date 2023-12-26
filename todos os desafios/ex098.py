# programa que tem uma função contador() que possui três parametros: inicio, fim, e passo, usando-os para uma contagem.
# o programa tem que realizar três contagens através da função criada:
# 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# e uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('=' * 40)
    if passo < 0:
        passo = passo * (-1)
    elif passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')

    if inicio > fim:
        fim -= 1
        passo = -passo
    else:
        fim += 1

    for c in range(inicio, fim, passo):
        sleep(0.25)
        print(f'{c}', end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez, personalize uma contagem! ')
i = int(input('INICIO: '))
f = int(input('FIM:    '))
p = int(input('PASSO:  '))
print()
contador(i, f, p)
print('='*40)
