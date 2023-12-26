from math import hypot

print('\nPara calcular o valor da hipotenusa em triangulo retangulo, escreva o valor dos catetos.')
c1 = float(input('  Cateto 1:'))
c2 = float(input('  Cateto 2:'))
print(f'\nCom catetos {c1} e {c2}, a hipotenusa vale {hypot(c1, c2)}.\n\nTchau!!!')
