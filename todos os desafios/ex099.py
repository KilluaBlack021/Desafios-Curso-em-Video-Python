# programa que tenha uma função chamada maior(). Ela receverá vários parametros com valores inteiros.
# seu programa tem que analisar todos os calores e dizer qual deles é o maior


def maior(num):
    resposta = int()
    for numeros in range(len(num)):
        if numeros == 0:
            resposta = num[0]
        elif resposta < num[numeros]:
            resposta = num[numeros]
    print(f'O maior número digitado foi {resposta}')


lista_de_numeros = list()
repeticoes = int(input('Quantos números vc deseja escrever: '))
while repeticoes != 0:
    for c in range(repeticoes):
        n = int(input('ESCREVA UM NúMERO: '))
        lista_de_numeros.append(n)
    repeticoes = int(input('Quer escrever mais quantos números(0 se não quiser mais): '))

maior(lista_de_numeros)
