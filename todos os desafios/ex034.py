# programa que calcula porcentagem de aumento de salario, se maior que R$ 3000, 10% de aumento, se menor 15%

salario = float(input('Escreva o valor de seu salario para que eu possa calcular o aumento: '))

if salario >= 3000:
    print(f'Seu aumento foi de 10%, seu salario de R${salario:,.2f}, agora é de R${salario * 1.10:,.2f}')
else:
    print(f'Seu aumento foi de 15%, seu salario de R${salario:,.2f}, agora é de R${salario * 1.15:,.2f}')

print('Tchau!!!')
