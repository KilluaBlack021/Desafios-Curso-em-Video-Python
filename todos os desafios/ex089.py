# programa que le nome e duas notas de varios alunos e guarda tudo numa lista composta. No fim
# mostra um 'boletim' contendo a média de cada aluno e permite que o usuario possa ou n mostra as notas individualmente

# lista master
alunos = []

print('='*40)
print(f'{" CADASTRO ":^40}')
print('='*40)

while True:
    nome = str(input('NOME: ')).strip().upper()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))

    aluno = [nome, nota1, nota2]
    # print(aluno)

    alunos.append(aluno[:])

    print('-'*40)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'NS':
        r = str(input('Tendi não!!!\nQuer continuar? [S/N] ')).strip().upper()
    if r == "N":
        break
    else:
        print('-'*40)

# perfumaria
print('\n\n\n')
print('='*40)
print(f'{" BOLETIM ":^40}')
print('='*40)
print(f'  {"NOME":^30}|{"MÉDIA":^8}')
# boletim
for c in range(len(alunos)):
    print('-'*40)
    print(f'{c+1}º{alunos[c][0].capitalize():^30}|{str((alunos[c][1] + alunos[c][2]) / 2):^8}')
print('='*40)

# nota em especifico
while True:
    nome_aluno = str(input(f'''Quer a nota de algum aluno em especifico? 
    
- Se SIM! [Digite o nome dele]
- Se NÂO! [Aperte "enter"] 
    
    R: ''')).strip().upper()
    print('='*40)
    if nome_aluno == '':
        break
    else:
        for p in range(len(alunos)):
            if nome_aluno in alunos[p]:
                dados_aluno = alunos[p][:]
                print(f'Aqui estão as notas do aluno {dados_aluno[0]}\n')
                print(f'NOTA 1: {dados_aluno[1]}')
                print(f'NOTA 2: {dados_aluno[2]}')
                print('=' * 40)
            if p - 1 == len(alunos):
                print('Não consegui encontrar o aluno!!!')
                print('=' * 40)
