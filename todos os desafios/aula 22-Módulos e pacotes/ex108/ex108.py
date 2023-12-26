from moeda import *


preco = float(input('Escreva o preço de um produto: R$ '))
aumento = int(input('Informe a taxa e aumento em %: '))
diminuicao = int(input('Informe a taxa e diminuição em %: '))

print(f'''

A partir dos dados informados obtemos estes resultados:

    - O dobro de {moeda(preco)} é {moeda(dobro(preco))}
    - A metade de {moeda(preco)} é {moeda(metade(preco))}
    - {moeda(preco)} com uma taxa de aumento de {aumento}% obtemos {moeda(aumentar(preco, aumento))}
    - {moeda(preco)} com uma taxa de diminuição de {diminuicao}% obtemos {moeda(diminuir(preco, aumento))}

''')
