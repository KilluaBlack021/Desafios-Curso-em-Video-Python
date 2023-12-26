# programa que calcula preço de viagem, se for mais de 200km, é R$0,45/km, mas se for menor é R$0,50/km

distancia = int(input('Qual a distancia em km que você percorrerá na sua viagem: '))
valor_a_pagar = 0.45 if distancia > 200 else 0.50

print(f'Em sua viagem de {distancia}km, você pagará R${valor_a_pagar * distancia:,.2f}')
