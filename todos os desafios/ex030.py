# programa que determina se um numero é par ou impar

numero = int(input('Escreva um número inteiro: '))

if numero % 2 > 0:
    print(f'O número {numero} é impar')
else:
    print(f'O número {numero} é par')
