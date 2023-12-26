# programa que mostre uma tabuada de varios numeros, um de cada vez para cada valor registrado. interrompe se num < 0

while True:
    num = int(input('Escreva algum número inteiro: (se for negativo o codigo para) '))
    if num < 0:
        break
    print('='*60)
    for c in range(10):
        print(f'{num:^10} X {c:^10} =         {num * c}')
    print('='*60)

print('Tchau!!!')
