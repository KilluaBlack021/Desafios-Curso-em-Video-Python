# programa que crie uma matriz 3x3 e a preenche com valores lidos pelo teclado. No fim
# mostre a matriz na tela como, uma matriz mesmo

matriz = [[], [], []]

for c in range(9):
    if c <= 2:
        n = float(input(f'Escreva um valor para [0, {c}]: '))
        matriz[0].append(n)
    elif c <= 5:
        n = float(input(f'Escreva um valor para [1, {c}]: '))
        matriz[1].append(n)
    elif c <= 8:
        n = float(input(f'Escreva um valor para [2, {c}]: '))
        matriz[2].append(n)

print(f'\n\n{" MATRIZ ":=^40}')
for coisas in range(3):
    for i in range(3):
        print(f'|{str(matriz[coisas][i]):^10}| ', end=' ')
    print('\n')
print('='*40)
