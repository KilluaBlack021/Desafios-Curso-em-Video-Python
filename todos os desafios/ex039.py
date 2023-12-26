# programa que indica se alguem ainda irá se alistar, se está na hora de se alistar ou se passou do tempo do alistamento

from datetime import date

idade = date.today().year - int(input('Escreva seu ano de nascimento: '))

if idade < 18:
    print(f'Você deverá se alistar em {18 - idade} anos. No ano de {date.today().year + 18 - idade}')
elif idade == 18:
    print('Você deve se alistar.')
else:
    print(f'Passou {idade - 18} anos do tempo de alistamento. No ano de {date.today().year - idade + 18}')
