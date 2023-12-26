import locale


def moeda(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor_formatado = locale.currency(float(valor), grouping=True)
    return valor_formatado


def resumo(valor, taxa_aumento, taxa_diminuicao):
    v = float(valor)
    print('\n\n')
    print('='*40)
    print('RESUMO DO VALOR'.center(40))
    print('='*40)
    print(f'''    Preço Analisado: \t {moeda(v)}
    Dobro do Preço: \t {dobro(v, True)}
    Metade do Preço: \t {metade(v, True)}
    {taxa_aumento:0>2}% de aumento: \t {aumentar(v, taxa_aumento, True)}
    {taxa_diminuicao:0>2}% de redução: \t {diminuir(v, taxa_diminuicao, True)}''')
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
        return moeda(float(valor / 2))
    else:
        return valor / 2
