# programa faz o cadastro de varias pessoas, para cada cadastro, pergunta se o usuario deseja cadastrar mais ou parar e
# mostrar quantas pessoas tem mais de 18 anos
# mostra quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

cont_idade = cont_homens = cont_mulheres_menores = 0

while True:
    print('='*30)
    # nome = str(input('Escreva o nome de uma pessoa: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO:  [M/F]')).strip().upper()
    while sexo not in "MF":
        sexo = str(input('Não entendi! Escreva novamente o sexo:   [M/F]')).strip().upper()

    # pessoas +18
    if idade > 18:
        cont_idade += 1

    # nº de homens cadastrados
    if sexo[0] == 'M':
        cont_homens += 1

    # nº mulheres < 20 anos
    if sexo[0] == 'F' and idade < 20:
        cont_mulheres_menores += 1

    print('-'*30)
    continua = str(input('Quer continuar? ')).strip().upper()
    while continua not in "NS":
        continua = str(input('Entendi não!\nQuer continuar?  [S/N] ')).strip().upper()
    if continua[0] == 'N':
        print('='*30)
        break


print(f'''
A partir dos dados informados, pode-se inferir que...

Há {cont_idade} pessoas maiores de 18 anos.
Há {cont_homens} homens cadastrados.
Há {cont_mulheres_menores} mulheres menores de 20 anos.


Tchau!!!
''')

