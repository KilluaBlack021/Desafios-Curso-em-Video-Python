# aprimoramento do ex093 para que ele funciona com varios jogadores, mostre detalhes de cada jogo se o user desejar

# programa que gerencia o aproveitamento de um jogador de futebol.
# o programa le o nome, Nº de partidas jogadas  por ele.
# le o Nº de gols por partida. No fim
# tudo é guardado em um dicionário incluindo total de gols feitos durante o campeonato

jogadores = list()
ficha = dict()
gols = []
tot_gols = 0

while True:
    print('=' * 40)
    nome = str(input('NOME: ')).strip()
    partidas = int(input('Nº partidas jogadas: '))

    if partidas == 0:
        gols.append(0)

    for g in range(partidas):
        gols_por_partida = int(input(f'Nº de gols na {g+1}º partida: '))
        tot_gols += gols_por_partida
        gols.append(gols_por_partida)

    # ficha técnica do jogador
    ficha['nome'] = nome
    ficha['partidas'] = partidas
    ficha['gols'] = gols
    ficha['total de gols'] = tot_gols

    jogadores.append(ficha.copy())

    print('-'*40)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in "SN":
        r = str(input('\033[31mNÂO ENTENDI!!!\033[m\nQuer continuar? [S/N] ')).strip().upper()
    if r == "N":
        break

# # mostrando tudo
print('\n\n\n')
print(f'{" FICHAS ":=^44}')
for coisas in range(len(jogadores)):
    print(f'\n\nJogador {coisas+1}:')
    print(f'''
    {'-' * 40}
    NOME:       {jogadores[coisas]['nome']}
    {'-' * 40}
    PARTIDAS:   {jogadores[coisas]['partidas']}
    {'-' * 40}
    GOLS:       {jogadores[coisas]['total de gols']}
    {'-' * 40}''')
print('='*44)

while True:
    j = int(input('Digite o Nº do jogador que deseja ver detalhes\n(ou 0 caso não queira!)\n R: '))
    while j > (len(jogadores)) or j < 0:
        print('\033[31mJogador não encontrado!!!\033[m')
        j = int(input('Digite o Nº do jogador que deseja ver \n(ou 0 caso não queira!)\n R: '))
    if j == 0:
        break
    else:
        print(f'')
        print('='*45)
        print(f'''
Mostrando detalhes do jogador {j-1}:

    NOME: {jogadores[j-1]['nome']}
    {'-' * 40}
    PARTIDAS: {jogadores[j-1]['partidas']}
    {'-' * 40}
    GOLS: {jogadores[j-1]['total de gols']}
    {'-' * 40}
    GOLS/PARTIDAS:''')
        for c in range(len(gols)):
            print(f'        - {c+1:0>3}ª partida foram {jogadores[j-1]["gols"][c]:<10}gols.')
        print('='*40)
