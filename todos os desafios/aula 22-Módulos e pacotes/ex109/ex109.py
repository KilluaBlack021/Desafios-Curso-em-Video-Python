from moeda import *


preco = float(input('Escreva o preço de um produto: R$ '))
aumento = int(input('Informe a taxa e aumento em %: '))
diminuicao = int(input('Informe a taxa e diminuição em %: '))

print(f'''

A partir dos dados informados obtemos estes resultados:

    - O dobro de {moeda(preco)} é {dobro(preco, True)}
    - A metade de {moeda(preco)} é {metade(preco, True)}
    - {moeda(preco)} com uma taxa de aumento de {aumento}% obtemos {aumentar(preco, aumento, True)}
    - {moeda(preco)} com uma taxa de diminuição de {diminuicao}% obtemos {diminuir(preco, aumento, True)}

''')
