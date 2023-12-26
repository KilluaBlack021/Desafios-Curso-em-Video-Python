# programa que tem uma função chamada area(). Ela recebe as dimensões de um terreno retangular e mostra a area dele


def area_retangulo(largura, comprimento):
    area = largura * comprimento
    return print(f'A area do terreno {largura}x{comprimento} é {area}')


larg = float(input('Escreva a largura de um terreno retangular: '))
comp = float(input('Escreva agora o seu comprimento: '))
area_retangulo(larg, comp)
