# programa que calcula preço do produto a partir da forma de pagamento:

desconto = 0
valor_do_produto = float(input('Valor do produto: '))
meio_de_pagamento = int(input('''
Forma de pagamento: 

    [1] à vista, cheque ou pix
    [2] debito
    [3] até 2x no cartão
    [4] 3x ou mais no cartão

R: '''))

if meio_de_pagamento == 1:
    desconto = 0.90
elif meio_de_pagamento == 2:
    desconto = 0.95
elif meio_de_pagamento == 3:
    desconto = 1
else:
    desconto = 1.20

print(f'\nO preço final do produto será R${valor_do_produto * desconto:,.2f} devido ao metodo de pagamento escolhido.')
