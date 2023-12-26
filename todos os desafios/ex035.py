# programa que diz se há a possibilidade de forma um triângulo a partir de 3 retas

r1 = float(input('Escreva um valor para a primeira reta: '))
r2 = float(input('Escreva um valor para a segunda reta: '))
r3 = float(input('Escreva um valor para a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Da para formar um triângulo com as retas: {r1}, {r2} e {r3}')
else:
    print('Não foi possivel formar um triângulo!')

print('Tchau!!!')
