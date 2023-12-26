# programa que mostra apenas a parte inteira de um numero do tipo float

from math import trunc

numero = float(input('Escreva um número real: '))
print(f'O número {numero} sem virgula, fica {trunc(numero)}.\n\nTchau!!!')
