# programa que o usuario possa digitar varios valores númericos, caso o número ja exista, ele n add. Por fim
# motra os valores de forma crescente

numeros = []
escolha = 'S'

while escolha not in 'N':
    n = int(input('Escreva um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Números adicionado com sucesso!')
    else:
        print('Número ja digitado! Não irei add')

    escolha = str(input('Quer continuar?  [S/N] ')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Não entendi!!!\nQuer continuar?  [S/N] ')).strip().upper()

print(f'Você digitados em ordem crescente foram: {sorted(numeros)}')
