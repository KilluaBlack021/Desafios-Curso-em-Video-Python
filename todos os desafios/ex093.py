# programa que gerencia o aproveitamento de um jogador de futebol.
# o programa le o nome, Nº de partidas jogadas  por ele.
# le o Nº de gols por partida. No fim
# tudo é guardado em um dicionário incluindo total de gols feitos durante o campeonato

ficha = dict()
gols = []
tot_gols = 0

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

print('='*90)
print(ficha)
print('='*90)

# mostrando tudo
print('\n\n\n')
print(f'{" FICHA TÉCNICA ":=^40}')
print(f'''NOME: {ficha['nome']}
{'-'*40}
PARTIDAS: {ficha['partidas']}
{'-'*40}
GOLS: {ficha['total de gols']}
{'-'*40}
GOLS/PARTIDAS:''')
for c in range(len(gols)):
    print(f'    - {c+1:0>3}ª partida foram {ficha["gols"][c]:<10}gols.')
print('='*40)
