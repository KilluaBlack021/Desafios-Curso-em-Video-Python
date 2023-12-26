# programa que lê um ano e diz se é bissexto ou não

ano = int(input('Escreva um ano ai: '))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} não é BISSEXTO!')

print('Tchau!!!')
