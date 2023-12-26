# Mostrarei a tabuada de um número que você digitará

# recebendo os valores
n = int(input('\nDigite um número inteiro( < 5 digitos) para ver sua tabuada: R$'))

# tabela
print('-'*26)
for c in range(0, 11, 1):
    print(f'{n:^5} x {c:^5} = {n*c}')
print('-'*26)
