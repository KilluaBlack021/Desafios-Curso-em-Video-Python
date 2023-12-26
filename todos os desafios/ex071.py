# programa que simula um caixa eletronico
# de acordo com o valor que o usuario deseja sacar, o programa mostra a quantidade de cedulas referente ao valor
# só pode cedulas de R$50, R$20, R$10 e R$1

valor_saque = int(input('Valor do saque: '))
cinquenta = vinte = dez = um = 0

valor = valor_saque
while True:
    while (valor - 50) >= 0:
        valor -= 50
        cinquenta += 1
    while (valor - 20) >= 0:
        valor -= 20
        vinte += 1
    while (valor - 10) >= 0:
        valor -= 10
        dez += 1
    while (valor - 1) >= 0:
        valor -= 1
        um += 1
    if valor >= 0:
        break

print(f'''
valor do saque: {valor_saque}
cedulas de cinquenta: {cinquenta}
cedulas de vinte: {vinte}
cedulas de dez: {dez}
cedulas de um: {um} 
''')
