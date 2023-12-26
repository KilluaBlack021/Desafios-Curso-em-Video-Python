def moeda(valor):
    sei_nao = f'R${valor:.2f}'
    return sei_nao


def aumentar(valor, taxa):
    return valor + (valor * (taxa / 100))


def diminuir(valor, taxa):
    return valor - (valor * (taxa / 100))


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2
