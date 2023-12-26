# programa que tem apenas uma unica tupla com nomes de produtos e seus respectivos preços na sequencia
# organize os preços de forma tabular

tupla = 'Sabonete', 2.99, 'KY', 19.99, 'Machonha', 10, 'Agua', 30.00, 'Play5', 2000000, 'Play4', 100000

print('='*41)
print(f'|{"Produtos":^20}|{"Preços":^20}')
print('='*41)
for i in range(0, len(tupla), 2):
    print(f' {tupla[i]:.<20}|R${tupla[i+1]:>17,.2f}')
print('-'*41)
