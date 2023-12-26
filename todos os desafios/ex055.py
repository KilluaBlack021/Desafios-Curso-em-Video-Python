# programa que le o peso de 5 pessoas, e diz qual é o maior e o menor peso

maior = menor = 0


for c in range(5):
    peso = float(input('Escreva o peso de 5 pessoas: '))
    maior = peso if peso > maior else maior
    menor = peso if peso < menor or menor == 0 else menor

print(f'''A partir do 5 valores indicados:

O maior peso foi: {maior}
O menor peso foi: {menor}
''')
