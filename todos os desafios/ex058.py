# joguinho que o pc "PENSA" em um número entre 0-10 e o jogador deve advinhar qual número é, e diz quantas tentativas

from random import randint

escolha_player = tentativas = 0
escolha_pc = randint(0, 11)

print('Acabei de pensar em um número entre 0 - 10, advinhe qual. ')
while escolha_pc != escolha_player:
    escolha_player = int(input('\nSeu palpite: '))
    tentativas += 1

print(f'Para acertar foram necessarios {tentativas} palpites, o número que pensei foi {escolha_pc}')
