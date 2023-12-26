# programa que mostra a média de uma quantidade de números indefinida, além do maior valor entre eles e o menor

maior = menor = soma = contador = 0
continua = 's'

while continua != 'N':
    numero_digitado = int(input('\n\nEscreva um número inteiro: '))

    # na primeira vez que rodar
    if contador == 0:
        maior = menor = numero_digitado
    else:
        # quem é maior ou menor
        if maior < numero_digitado:
            maior = numero_digitado
        if menor > numero_digitado:
            menor = numero_digitado

    # primeira parte da média
    soma += numero_digitado
    # segunda parte da média
    contador += 1

    # continua?
    continua = str(input('\nSe você não deseja escrever mais números, escreva "N ou n": ')).strip().upper()

# resultados
print(f'''
A média dos números digitados foi: {soma / contador}
O maior número é: {maior}
O menor número é: {menor}
''')
