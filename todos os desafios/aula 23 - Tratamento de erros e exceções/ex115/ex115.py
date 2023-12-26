from funcoes import *

while True:
    # menu principal
    print('\n\n')
    linha(True)
    print('MENU PRINCIPAL'.center(60))
    linha(True)

    # opções
    colorir('1 - Ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair do programa', 34)
    linha()

    # verificação de dados
    while True:
        op = str(input('\033[32mSua Opção: \033[m'))
        if op != '1' and op != '2' and op != '3':
            colorir('OPÇÃO INVALIDA!!!', 31)
        else:
            break

    # pessoas cadastradas
    if op == '1':
        ver_cadastros()

    # cadastrar alguem
    elif op == '2':
        print('\n')
        linha(True)
        print('CADASTRANDO NOVA PESSOA'.center(60))
        linha()
        n = str(input('NOME: ')).strip().upper()
        i = leia_int()
        linha()
        cadastrar(nome=n, idade=i)

    # saida
    elif op == '3':
        break
