# programa que pergunta uma função interna do python e retorna seu manual

from time import sleep


def manual(comando):
    print(f'\033[1mMostrando MANUAL de \033[31m{comando}\033[m ', end='')
    for c in range(3):
        sleep(1)
        print('.', end='')
    print('\n\n')
    return help(comando)


def linha_azul():
    print('\033[34m=\033[m' * 60)


while True:
    linha_azul()
    print(f'\033[1;34m{"SISTEMA DE AJUDA PyHELP":^60}\033[m')
    linha_azul()
    funcao = str(input('\033[34mFunção ou Biblioteca >\033[m '))
    linha_azul()
    if funcao.upper() == 'FIM':
        print('\033[33mAté um outro dia, amigo! Você é um amigo!!!')
        linha_azul()
        break
    else:
        manual(funcao)
