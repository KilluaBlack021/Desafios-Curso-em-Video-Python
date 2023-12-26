def leia_dinheiro():
    while True:
        valor = str(input('Escreva o preço de um produto: R$ ').replace(',', '.').strip())
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO! "{valor}" é um valor inválido! \033[m')
        else:
            return float(valor)
