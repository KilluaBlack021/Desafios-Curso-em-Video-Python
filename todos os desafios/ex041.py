# programa classifica a categoria de atletas de natação a partir da sua data de nascimento

from datetime import date

idade = date.today().year - int(input('Escreva seu ano de nascimento: '))
categoria = ''

if idade < 9:
    categoria = 'MIRIM'
elif idade < 14:
    categoria = 'INFANTIL'
elif idade < 19:
    categoria = 'JUNIOR'
elif idade < 20:
    categoria = 'SêNIOR'
else:
    categoria = 'MASTER'

print(f'A partir da sua idade que é de {idade} anos, a sua categoria corresponde à {categoria}.')
