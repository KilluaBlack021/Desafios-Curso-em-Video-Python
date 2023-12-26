def moeda(valor):
    sei_nao = f'R${valor:.2f}'
    return sei_nao


def resumo(valor, taxa_aumento, taxa_diminuicao):
    print('\n\n\n\n')
    print('='*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('='*40)
    print(f'''    Preço Analisado:    {moeda(valor)}
    Dobro do Preço:     {dobro(valor,  True)}
    Metade do Preço:    {metade(valor, True)}
    {taxa_aumento:0>2}% de aumento:     {aumentar(valor, taxa_aumento, True)}
    {taxa_diminuicao:0>2}% de redução:     {diminuir(valor, taxa_diminuicao, True)}''')
    print('=' * 40)


def aumentar(valor, taxa, moeda_format=False):
    if moeda_format:
        return moeda(valor + (valor * (taxa / 100)))
    else:
        return valor + (valor * (taxa / 100))


def diminuir(valor, taxa, moeda_format=False):
    if moeda_format:
        return moeda(valor - (valor * (taxa / 100)))
    else:
        return valor - (valor * (taxa / 100))


def dobro(valor, moeda_format=False):
    if moeda_format:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, moeda_format=False):
    if moeda_format:
        return moeda(valor / 2)
    else:
        return valor / 2
