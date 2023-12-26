# programa que le o nome e preço de varios produtos e pergunta se o usuario deseja add mais algum, mostrando no fim
# total gasto
# nº produtos custando mais de 1000
# nome do produto mais barato

nome_produto_mais_barato = ''
mais_barato = tot_gasto = n_produtos_menores_que_mil = contador = 0

while True:
    print('='*30)
    nome = str(input('NOME: ')).strip().upper()
    preco = float(input('PREÇO: '))

    # total gasto
    tot_gasto += preco

    # produtos menores que mil reais
    if preco < 1000:
        n_produtos_menores_que_mil += 1

    # nome produto mais barato
    if mais_barato == 0 or mais_barato > preco:
        nome_produto_mais_barato = nome
        mais_barato = preco

    # quer continuar?
    print('-'*30)
    continua = str(input('Quer continuar? [S/N]')).strip().upper()
    while continua not in 'SN':
        continua = str(input('Entendi não! Quer continuar? [S/N]')).strip().upper()
    if continua[0] == 'N':
        break

print(f'''
TOTAL GASTO: {tot_gasto}
PRODUTOS < 1000,00: {n_produtos_menores_que_mil}
PRODUTO MAIS BARATO: {nome_produto_mais_barato}
''')
