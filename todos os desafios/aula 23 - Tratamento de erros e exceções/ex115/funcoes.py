from time import sleep


def linha(linha_grossa=False):
    if not linha_grossa:
        print('-' * 60)
    else:
        print('='*60)


def colorir(txt, cor):
    print(f'\033[{cor}m{txt}\033[m')


def leia_int():
    while True:
        num = input('IDADE: ').strip()
        try:
            return int(num)
        except ValueError:
            if num == '':
                linha()
                colorir('Nenhum valor foi digitado pelo usuario. Considerando valor "0"', 33)
                return 0
            colorir(f'O valor "{num}" não é um número inteiro.', 31)


def ver_cadastros():
    print('\n')
    linha(True)
    print('CADASTROS'.center(60))
    linha(True)
    # tenta ler o arquivo cadastros.txt
    try:
        with open('cadastros.txt', 'r') as arquivo:
            contador = 0
            for linhas in arquivo:
                if linhas != '':
                    contador += 1
                print(linhas)
            if contador == 0:
                colorir('!!! Cadastros.txt encontra-se vazio, adicione pessoas !!!', 33)
    # caso eu não ache o arquivo cadastros.txt ele cria
    except FileNotFoundError:
        with open('cadastros.txt', 'w'):
            colorir('!!! cadastros.txt NÃO ENCONTRADO !!!', 33)
            sleep(1)
            colorir('!!! cadastros.txt CRIADO COM SUCESSO !!!', 34)
            sleep(1)
    linha(True)


def cadastrar(nome='<desconhecido>', idade=0):
    try:
        with open('cadastros.txt', 'a') as arquivo:
            arquivo.write(f' - {nome:.<47}{idade:>4} anos.' + '\n')
    except FileNotFoundError:
        with open('cadastros.txt', 'w'):
            colorir('!!! cadastros.txt NÃO ENCONTRADO !!!', 33)
            sleep(1)
            colorir('!!! cadastros.txt CRIADO COM SUCESSO !!!', 34)
            sleep(1)

        with open('cadastros.txt', 'a') as arquivo:
            arquivo.write(f' - {nome:.<47}{idade:>4} anos.' + '\n')

    colorir(f'{nome} adicionado(a) com sucesso!!!'.center(60), 32)
    linha(True)
