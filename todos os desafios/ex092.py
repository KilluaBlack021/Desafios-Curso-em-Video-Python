# programa que lê nome, ano de nascimento e carteira de trabalho, depois cadastra com idade em um dicionario
# se a CTPS for diferente de zero, o dicionario receberá o ano de contratação e o salário
# calcula e acrescenta, além da idade, a idade que ela irá se aposentar.

from datetime import date

print(f'{" CADASTRO ":=^40}')
nome = str(input('NOME: ')).strip()
print('-'*40)
nascimento = int(input('ANO DE NASCIMENTO: '))
print('-'*40)
ctps = int(input('CTPS (aperte 0 se não tiver): '))

pessoa = {
    'nome': nome,
    'idade': date.today().year - nascimento
}

# se vc é vagabundo ou não
if ctps > 0:
    print('-' * 40)
    ano_contratacao = int(input('ANO de CONTRATAÇÃO: '))
    while (ano_contratacao - nascimento) < 14:
        print('-'*40)
        ano_contratacao = int(input('\033[31mIdade de contratação invalida!\033[m\nANO de CONTRATAÇÃO: '))
    print('-' * 40)
    salario = float(input('SALARIO: '))

    if (date.today().year - ano_contratacao) > 35:
        prazo_aposentadoria = str('Você pode se aposentar! Tens mais de 35 anos de contribuição!')
    else:
        prazo_aposentadoria = int(ano_contratacao + 35 - nascimento)

    pessoa['ctps'] = ctps
    pessoa['ano de contratacao'] = ano_contratacao
    pessoa['salario'] = salario
    pessoa['idade de aposentadoria'] = prazo_aposentadoria

# resultado
print('\n\n')
print('=' * 40)
print(f'{" DADOS ":=^40}')
print('=' * 40)
print(f'''NOME: {pessoa['nome']}
IDADE: {pessoa['idade']}''')

if ctps > 0:
    print(f'''CARTEIRA DE TRABALHO: {pessoa['ctps']}
ANO DE CONTRATAÇÃO: {pessoa['ano de contratacao']}
SALARIO: {pessoa['salario']}
APOSENTADORIA: {pessoa['idade de aposentadoria']} anos''')
else:
    pessoa['ctps'] = 'BRANCA'
    print(f'CARTEIRA DE TRABALHO: {pessoa["ctps"]}')
print('=' * 40)
