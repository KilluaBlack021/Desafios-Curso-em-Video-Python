# programa que le o ano de nascimento de 7 pessoas, depois mostra quem é maior e quem é menor de 21 anos

from datetime import date

contador = 0


for c in range(7):
    idade = date.today().year - int(input('Escreva o ano de nascimento de alguem: '))
    if idade >= 21:
        contador += 1

print(f'De acordo com os anos de nascimento indicados, {contador} pessoas são maiores de 21 anos, '
      f'{7 - contador} não são.')
