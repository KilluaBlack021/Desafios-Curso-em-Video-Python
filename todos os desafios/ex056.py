# programa que lê nome, idade e sexo de 4 pessoas, e no final
# mostra a média de idade do grupo
# nome do homem mais velho
# n mulheres com menos de 20 anos.

nome_homem_mais_velho = ''
soma = n_mulheres = 0
mais_velho = 0

# main
for c in range(4):
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: [M/m]masculino    [F/f]feminino\n R: ')).strip().upper()

    # media de idade do grupo
    soma += idade

    # homem mais velho
    if idade > mais_velho and sexo == "M":
        mais_velho = idade
        nome_homem_mais_velho = nome

    # mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        n_mulheres += 1


print(f'''A partir dos dados adquiridos notasse que:

A MEDIA DE IDADES É:                        {soma / 4}
O HOMEM MAIS VELHO É:                       {nome_homem_mais_velho}
Nº DE MULHERES COM MENOS DE 20 ANOS É:      {n_mulheres}

''')
