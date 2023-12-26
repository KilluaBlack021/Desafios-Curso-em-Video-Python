# programa que lê o nome de uma cidade e diz se ela começa ou não com o nome "santo"

cidade = str(input('Escreva o nome de uma cidade: ')).strip().lower()
city = cidade.split()
if "santo" in city[0]:
    print(f'A cidade {cidade}, começa com "santo"')
else:
    print(f'A cidade {cidade}, não começa com "santo"')
