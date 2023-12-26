# APRIMORAMENTO DO EX086

# EX086
# programa que crie uma matriz 3x3 e a preenche com valores lidos pelo teclado. No fim
# mostre a matriz na tela como, uma matriz mesmo

matriz = [[], [], []]

for c in range(9):
    if c <= 2:
        n = float(input(f'Escreva um valor para [0, {c}]: '))
        matriz[0].append(n)
    elif c <= 5:
        n = float(input(f'Escreva um valor para [1, {c-3}]: '))
        matriz[1].append(n)
    elif c <= 8:
        n = float(input(f'Escreva um valor para [2, {c-6}]: '))
        matriz[2].append(n)

print(f'\n\n{" MATRIZ ":=^40}')
for coisas in range(3):
    for i in range(3):
        print(f'|{str(matriz[coisas][i]):^10}| ', end=' ')
    if coisas == 2:
        print('\n', '=' * 40)
    print('\n')


# COOMEÇO DO EX087
soma_pares = soma_terceiraColuna = maior = contador = 0
for i, v in enumerate(matriz):
    print(i)
    print(v)
    # mostre a soma de todos os valores pares digitados
    if v[i] % 2 == 0:
        soma_pares += v[i]

    # mostre a soma dos valores da terceira coluna
    soma_terceiraColuna += matriz[i][2]

    # o maior valor da segunda linha
    if matriz[1][i] > maior:
        maior = matriz[1][i]


print(f'''
A soma de todos os números pares: {soma_pares}
A soma dos valores da terceira coluna é: {soma_terceiraColuna}
O maior valor da segunda linha é: {maior}
''')
