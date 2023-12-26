# programa que lê um número inteiro e converte-o para binario ou octal ou hexadecimal

print('-=' * 30)
numero = int(input('Escreva um número inteiro: '))
neo_numero = 0
base = ''

while True:
    print('-' * 60)
    opcao = int(input(f'''Para que base você deseja converter o número {numero}?  

 [1] binario
 [2] octal 
 [3] hexadecimal

R:  '''))

    if opcao == 1:
        neo_numero = bin(numero)[2:]
        base = 'BINARIO'
        break
    elif opcao == 2:
        neo_numero = oct(numero)[2:]
        base = 'OCTAL'
        break
    elif opcao == 3:
        neo_numero = hex(numero)[2:]
        base = 'HEXADECIMAL'
        break
    else:
        print('!!! OPÇÃO INVALIDA !!!')

print(f'O número {numero} em {base} é: {neo_numero}')
