# o programa conta o numero de unidades, dezenas, centenas e unidade de milhar de um número inteiro

numero = int(input('Escreva um número entre 0 e 9999: '))
print(f'''
Unidade: {numero // 1 % 10}
Dezena: {numero // 10 % 10}
Centena: {numero // 100 % 10}
Milhar: {numero // 1000 % 10}

Tchau!!! ''')
