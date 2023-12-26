# simulador de aluguel de carro

kmRodados = int(input('Quantos km você rodou com o carro? \n R:'))
dias = int(input('Quantos dias você usou o carro? \n R:'))
valorTotal = float((kmRodados * 0.15) + (dias * 60))

print(f'\nO valor total a pagar pelo veiculo é de R${valorTotal:.2f}\n\nTchau!!!')
