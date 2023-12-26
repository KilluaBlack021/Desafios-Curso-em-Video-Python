# programa que lê um número e mostra seu fatorial

n = int(input('Escreva um número para que eu mostre seu fatorial: '))
c = n
resultado = 1
    
print(f'{n}! = {c}', end='')
while c != 1:
    resultado = resultado * c
    c -= 1
    print(f'x{c}', end='')

print(f' = {resultado}')
