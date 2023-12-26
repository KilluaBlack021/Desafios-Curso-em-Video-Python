# programa que mostra o valor do seno e do cosseno a partir de um angulo lido

from math import sin, cos, tan, radians


print('-='*40)
angulo = float(input('Escreva um angulo para achar o respectivo valor para seno, cosseno e tangente:'))
print('-='*40)
print(f'Seno      de {angulo}º é {sin(radians(angulo))}')
print(f'Cosseno   de {angulo}º é {cos(radians(angulo))}')
print(f'Tangente  de {angulo}º é {tan(radians(angulo))}')
print('-'*80)
