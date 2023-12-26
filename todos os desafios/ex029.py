# programa que imita um radar. A velocidade maxima é 80km/h, se passar, ele é multado em 7/km a mais

velocidade = int(input('Qual a velocidade do veiculo: '))
diferenca = velocidade - 80

print(f'\nSua velocidade é de {velocidade}km/h.\n')
if diferenca >= 1:
    print(f'---Você foi multado em ' + f'{diferenca * 7:,.2f} reais---')
