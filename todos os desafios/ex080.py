# programa que o usuario digita 5 valores e eles são cadastrados em uma lista ja na posição correta, sem usar o sort
# mostre a lista ordenada na tela

numeros = []

for c in range(0, 5):
    n = int(input('Escreva um número: '))
    if c == 0:
        numeros.append(n)
    else:
        if n > max(numeros):
            numeros.append(n)
        elif n < min(numeros):
            numeros.insert(0, n)
        elif n > numeros[c]:
            numeros.insert(c, n)

print('='*30)
print(numeros)
