# programa que le 1 termo e a razão para uma P.A e mostrará seus 10 primeiros números

termo = int(input('Escreva o primeiro número de uma P.A: '))
razao = int(input('Escreva a razão dessa P.A: '))
print('Os dez primeiros termos dessa P.A são: ', end='')
for c in range(9):
    print(termo, end=', ')
    termo += razao
print(termo, end='.')
