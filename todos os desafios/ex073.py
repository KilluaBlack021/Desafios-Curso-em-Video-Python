# o programa terá uma tupla com os colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostra
# os 5 primeiros colocados
# os ultimos 4
# uma lista com os times em ordem alfabetica
# a posição na tabela está o time Vasco

# atual no dia 14/12/2023
times = ('Palmeiras', 'Gremio', 'Atletico-MG', 'Flamengo', 'Botafogo', 'RB Bragantino', 'Fluminense',
         'Atletico Paranaense', 'Internacional', 'Fortaleza EC', 'Sao Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro',
         'Vasco DA Gama', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'America Mineiro')

print(f'''
a lista de times do Brasileirão: {times}\n
O top 5: {times[:5]}\n
Os piores 4: {times[-4:]}\n
Times em ordem alfabetica: {sorted(times)}\n
Posição Vasco: {times.index('Vasco DA Gama') + 1}º\n
''')
