# programa que analisa os parenteses de uma expressão matematica, e informa se ela está correta ou não

condicao = ''
expressao = str(input('Digite uma expressão matemática'))

# METODO 2
cont = 0

for i in expressao:
    if i == '(':
        cont += 1
    elif i == ')':
        cont -= 1
    if cont == -1:
        condicao = 'Invalida!!!'
        break
    elif cont != 0:
        condicao = 'Invalida!!!'
    else:
        condicao = 'Valida!!!'

print(f'\nA expressão: {expressao}\nSe encontra {condicao}')


# NÃO GOSTEI DESSE METODO, SE ALGUEM POR ))2*3( - 1( * 9 DA CERTO

# lista1 = []
# lista2 = []

# for i in expressao:
#     if i == '(':
#         lista1.append(i)
#     elif i == ')':
#         lista2.append(i)
#
# if len(lista1) != len(lista2):
#     condicao = 'Expressão invalida!!!'
# elif len(lista1) == len(lista2):
#     condicao = 'Expressão valida!!!'
