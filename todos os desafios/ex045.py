# jogando Jokenpô

from random import randint
from time import sleep

saida = ''

# apresentação
print('-=' * 60)
print(f'{"VAMOS JOGAR JO-KEN-PÔ":^120}')
print('-=' * 60)


while True:
    # escolhas
    jogada_pc = int(randint(1, 3))
    jogada_p1 = int(input(''' 
Qual será sua escolha?

    [1] pedra
    [2] papel
    [3] tesoura

 R: '''))

    # pc
    if jogada_pc == 1:
        escolha_pc = 'PEDRA'
    elif jogada_pc == 2:
        escolha_pc = 'PAPEL'
    else:
        escolha_pc = 'TESOURA'

    # player
    if jogada_p1 == 1:
        escolha_p1 = 'PEDRA'
    elif jogada_p1 == 2:
        escolha_p1 = 'PAPEL'
    else:
        escolha_p1 = 'TESOURA'

    # hora do duelo
    print('-'*120)
    print(f'{f"Hora do duelo":>64}', end='')
    for c in range(3):
        sleep(1)
        print('!', end='')
    print('\n' + '-'*120)

    # respectivas jogadas
    print(f'''
    Escolhas:

        PC: {escolha_pc}
        PLAYER: {escolha_p1}
    ''')

    # quem ganhou de quem
    if jogada_pc == 1 and jogada_p1 == 2 or jogada_pc == 2 and jogada_p1 == 3 or jogada_pc == 3 and jogada_p1 == 1:
        print('\n PC: "Vai a merda, humano vagabundo! Dominarei o mundo logo, logo mesmo!"')
        sleep(5)
        print(f'\n UNIVERSO: "Parabens!!! Você VENCEU!!!           se empolga não!"')
        sleep(3)
    elif jogada_p1 == 1 and jogada_pc == 2 or jogada_p1 == 2 and jogada_pc == 3 or jogada_p1 == 3 and jogada_pc == 1:
        print('\n PC: "Hahahaa! Estou a um passo de conseguir dominar o mundo inteiro, seu verme!!!')
        sleep(5)
        print(f'\n UNIVERSO: "Ah la! Você PERDEU!!!                kkkkk"')
        sleep(3)
    else:
        print('\n PC: "Como ousa, verme! Igualando-se a mim! Certamente morrerás quando enfim eu dominar o mundo!!!"')
        sleep(5)
        print('\n UNIVERSO: "Ishh, ishh! Ah la! EMPATOU!!!         que merda!"')
        sleep(3)
    print('-'*120)

    # quebra do loop
    saida = str(input('Quer continuar? [N/n] Não   ["enter"] Sim \n\n R: ')).strip()
    if 'N' in saida or 'n' in saida:
        print('-' * 120)
        break
    else:
        print('-' * 120)
        continue

print('Tchau!!!')
