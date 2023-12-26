# programa que tem uma função chamada factorial() que recebe dois parâmetros:
# 1º Numero e o 2º é o show(serve para mostrar o calculo na tela)

def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: É o número que queremos saber o fatorial
    :param show: Se queremos ver o processo
    :return: O resultado
    """
    if not show:
        for c in range(n-1, 0, -1):
            n *= c
        return n
    elif show:
        for c in range(n, 1, -1):
            print(f'{c} X', end=' ')
        print('1 = ', end='')
        return fatorial(n)


print(fatorial(5, True))
help(fatorial)
