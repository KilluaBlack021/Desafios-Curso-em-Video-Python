# programa que analisa a média de um aluno e diz sua situação

situacao = ''
nota1 = float(input('Escreva a primeria nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2


if media < 5:
    situacao = 'REPROVADO'
elif media < 7:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'APROVADO'

print(f'Com uma média de {media:.1f}, com base nas notas {nota1:.1f} e {nota2:.1f}, você se encontra: {situacao}!!!')
