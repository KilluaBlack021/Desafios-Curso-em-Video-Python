# programa que tem uma função voto() que recebe parametros, o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições

from datetime import date


def voto(n):
    idade = date.today().year - n
    if idade < 16:
        return f'Com {idade} anos. NÃO VOTA!!!'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos. VOTO OPCIONAL!!!'
    else:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO!!!'


nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))
