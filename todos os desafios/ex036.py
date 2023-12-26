# programa que aprova um emprestimo bancario a partir do salario do comprador e o valor de cada prestação

emprestimo = ''
salario = float(input('Digite o valor referente a sua renda mensal: ')) * 0.3
valor_do_imovel = float(input('Digite o valor referente ao imovel: '))
tempo_para_pagar = int(input('Tempo esperado (em meses) para pagar o emprestimo: '))
prestacao_mensal = float(valor_do_imovel / tempo_para_pagar)

if salario < prestacao_mensal:
    emprestimo = 'NEGADO'
else:
    emprestimo = 'APROVADO'

print(f'O emprestimo foi {emprestimo}, visto os dados apresentados! \n\n\nTchau!!!')
