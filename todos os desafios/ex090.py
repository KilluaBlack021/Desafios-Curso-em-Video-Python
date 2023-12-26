# programa que le nome e média de um aluno, guarda tbm sua situação referente a sua média em um dicionario. No fim
# mostra a estrutura na tela

nome = str(input('NOME: ')).strip().upper()
media = float(input(f'MÉDIA de {nome}: '))

if media < 5:
    situacao = 'REPROVADO!'
elif media < 7:
    situacao = 'RECUPERAÇÃO!!'
elif media <= 10:
    situacao = 'APROVADO!!!'
else:
    situacao = '???? NÂO FAZ SENTIDO !!!!'


aluno = {'nome': nome.strip().upper(), 'media': media, 'situacao': situacao}

print(f'O aluno {aluno["nome"]}, com média igual a {aluno["media"]} se encontra {aluno["situacao"]}')
