# o programa lê 3 números e fala qual é o maior e o menor

numeros = []
menor = maior = 0

for c in range(3):
    n = float(input(f'Escreva o {c + 1}º número: '))
    numeros.append(n)
    menor = numeros[c] if menor > numeros[c] or menor == 0 else menor
    maior = numeros[c] if maior < numeros[c] or maior == 0 else maior

print(f'''
Numeros: {numeros}
Maior Nº: {maior}
Menor Nº: {menor}
''')
