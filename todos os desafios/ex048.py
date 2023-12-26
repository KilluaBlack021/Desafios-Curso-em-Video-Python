# programa que calcula a soma de todos os números impares multiplios de 3 entre 1-500

soma = 0
for c in range(1+2, 500, 3):
    soma += c

print(f'A soma de todos os números impares multiplios de 3 entre 1-500 é: {soma}')
