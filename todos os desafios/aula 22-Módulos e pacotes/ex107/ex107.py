from moeda import *


valor = float(input('Escreva um número: '))
aumento = int(input('Informe a taxa e aumento em %: '))
diminuicao = int(input('Informe a taxa e diminuição em %: '))

print(f'''

A partir dos dados informados obtemos estes resultados:

    - O dobro de {valor} é {dobro(valor)}
    - A metade de {valor} é {metade(valor)}
    - {valor} com uma taxa de aumento de {aumento}% obtemos {aumentar(valor, aumento)}
    - {valor} com uma taxa de diminuição de {diminuicao}% obtemos {diminuir(valor, aumento)}

''')
