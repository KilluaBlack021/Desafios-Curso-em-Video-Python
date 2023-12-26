def moeda(valor):
    sei_nao = f'R${valor:.2f}'
    return sei_nao


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

