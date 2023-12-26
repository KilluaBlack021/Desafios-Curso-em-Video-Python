# programa que le 6 nº inteiros e mostra a soma dos nº pares.

soma = 0
numeros = []
for c in range(6):
    n = int(input('Escreva algum número inteiro: '))
    numeros.append(n)
    if n % 2 == 0:
        soma += n

print(f'Os números lidos foram: {numeros}\nA soma entre eles foi: {soma}')
