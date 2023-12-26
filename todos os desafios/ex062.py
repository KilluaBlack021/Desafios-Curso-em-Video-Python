# refazendo o desafio 051

n = objetivo = 10

termo = int(input('Escreva o primeiro número de uma P.A: '))
razao = int(input('Escreva a razão dessa P.A: '))
print('Os dez primeiros termos dessa P.A são: ', end='')

while n != 1:
    print(termo, end=', ')
    termo += razao
    n -= 1
print(termo, end='.')

print('\n\n\nMais quantos elementos dessa PA você quer que eu mostre: ')
objetivo = int(input(' R: '))
while n != objetivo + 1:
    print(termo, end=', ')
    termo += razao
    n += 1
    if n == objetivo + 1:
        print(termo, end='.')
