# programa que tem uma função chamada ficha(), ela recebe dois parãmetros opcionais: o nome e o Nº de gols de um jogador
# o programa deverá mostrar a ficha do jogador, msm qeu algum dados não tenha sido informado corretamente

def ficha(n='<desconhecido>', g=0):
    """
    -> Programa que cria uma ficha para um jogador
    :param n: Nome do jogador
    :param g: Nº de gols
    :return: resultado
    """
    print(f'O jogador {n} fez {g} gols.')


nome = str(input('NOME do jogador: ')).strip()
gols = str(input('Nº de GOLS: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
