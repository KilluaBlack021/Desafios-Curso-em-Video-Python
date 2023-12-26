# calculadora esquisita

opt = 4

while 6 < opt < 0 or opt == 4:
    print('=='*60)
    valor1 = float(input('Escreva o primeiro valor: '))
    valor2 = float(input('Escreva o segundo valor: '))

    opt = int(input('''O que deseja fazer com os dois números?

    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números 
    [5] ir embora

 R: '''))

    if opt == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
    elif opt == 2:
        print(f'O produto dos número {valor1} e {valor2} é: {valor1 * valor2}')
    elif opt == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2}, o maior é {valor1}')
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2}, o maior é {valor2}')
        else:
            print('Ambos são iguais')
    elif opt == 5:
        print('Ok então! Tchau!!!')
    else:
        opt = 4
