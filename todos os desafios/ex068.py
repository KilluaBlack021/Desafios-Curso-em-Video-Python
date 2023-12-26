# programa que joga par ou impar. O jogo só para quando o jogador perder

from random import randint

contador = 0

while True:
    # obtenção de dados
    impopar = str(input('Você quer [I]imper ou [P]par? ')).strip().upper()
    pc_escolha = int(randint(0, 11))
    player_escolha = int(input('Escreva um número inteiro de 0-10: '))

    # pra não chorarem
    print(f'''
O COMPUTADOR ESCOLHEU: {pc_escolha}
TU ESCOLHESTES: {player_escolha}
A SOMA dá {pc_escolha + player_escolha}, um número ''', end='')

    # deu oq
    if (pc_escolha + player_escolha) % 2 == 0:
        deu_oq = 'PAR. Portanto...'
    else:
        deu_oq = 'IMPAR. Portanto...'
    print(deu_oq)

    # quem ganhou oq
    if impopar[0] == deu_oq[0]:
        print('\nParabens! Você VENCEU!')
        contador += 1
        print('-'*90)
    else:
        print('\nParabens! Você PERDEU! Ent... tchau!!!')
        break

print('='*90)
print(f'Você ganhou {contador} vezes consecutivas.')
