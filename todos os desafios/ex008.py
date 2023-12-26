# conversor de metro para centimetro e milimetro

n = float(input('\nDigite um valor em metros(até 9 digitos) para converte-lo para centimetro e milimetro: '))

print('-'*129)
print(f'|{"Metros":^40} | {"Centimetro":^40} | {"Milimetro":^40} |')
print('-'*129)
print(f'|{n:^40} | {n*100:^40} | {n*1000:^40} |')
print('-'*129)
print('\nTchau!!!')
