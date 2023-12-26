# programa que tenha um tupla com um contagem regressiva de zero a vinte
# o programa deverá ler um número pelo teclado(0-20) e mostra-lo por extenso

numeros = ('Vinte', 'Dezenove', 'Dezoito', 'Dezesete', 'Dezeseis', 'Quinze', 'Quatorze', 'Treze', 'Doze', 'Onze', 'Dez',
           'Nove', 'Oito', 'Sete', 'Seis', 'Cinco', 'Quatro', 'Três', 'Dois', 'Um', 'Zero')

n = -1
while n > 20 or n < 0:
    n = int(input('Escreva um número de 0-20: '))
print(f'O número {n} por extenso é: {numeros[-n - 1]}')
