# programa que 4 jogadores jogam um dado com resultados aleatórios, sendo guardados em um dicionario. Por fim
# o dicionario deve ser mostrado em ordem e o vencedor deverá ter tirado o maior número no dado

from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

# mostrando bonitinho
print('='*30)
for k, v in jogo.items():
    print(f'O {k} jogou {v} no dado.')
print('='*30)

# fazendo o ranking
print()
print(f'{" RANKING ":=^39}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} que tirou {v[1]} no dado.')
