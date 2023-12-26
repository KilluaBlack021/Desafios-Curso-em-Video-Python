# programa que ajuda um jogador da mega sena a criar palpites.
# ele pergunta quantos jogos serão gerados e sorteia 6 números entre 1-60 para cada jogo
# coloca tudo isso ai numa lista composta

from random import randint

palpites = list()


n_jogos = int(input('Nº de palpites você quer: '))
for c in range(n_jogos):
    palpite = []
    for n in range(6):
        while True:
            p = f'{str(randint(1, 61)):^2}'
            if p not in palpite:
                palpite.append(p)
                break
    palpites.append(palpite[:])

print('\n')
print(f'{" PALPITES ":=^41}')
# palpites
for jogos in range(len(palpites)):
    print(f'{jogos+1}º', end=' ')

    # numeros
    for numeros in range(6):
        print(f'{int(palpites[jogos][numeros]):^6}', end='')

    if jogos != len(palpites) - 1:
        print('\n', '-'*40)
    else:
        print('')
        print('='*41)
