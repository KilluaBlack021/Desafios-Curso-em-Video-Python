# programa que escolhe um número ente 0 e 5, se o usuario acertar qual o número, mostra "vence", senão "perde"

from random import randint

while True:
    indagacao_usuario = -1
    print('-' * 65 + '\nEstou pensando em um número entre 0 - 5... Qual você acha que é?')
    n = int(randint(0, 5))
    while 0 > indagacao_usuario or indagacao_usuario > 5:
        indagacao_usuario = int(input('\nEscreva o número entre 0-5: '))
    if indagacao_usuario == n:
        print('\n---Você VENCEU!!!---\n')
    else:
        print('\n---Você PERDEU!!!---\n')

    continuacao = str(input('-' * 65 + '\nQuer continuar? Se não quiser digite: [N/n]')).strip().lower()
    if 'n' in continuacao:
        break
    else:
        continue

print('Tchau!!!')
