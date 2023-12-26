# programa que a relação entre dois números, se um é maior ou menor que outro, ou são iguais

n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva outro número: '))

if n1 > n2:
    print(f'{n1} (o primeiro valor) é maior que {n2}(o segundo valor).')
elif n1 < n2:
    print(f'{n2} (o segundo valor) é maior que {n1}(o primeiro valor).')
else:
    print('Ambos os números são iguais.')

print('Tchau!!!')
