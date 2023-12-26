# programa que lê varios números inteiros, só parando quando o valor 0 é digitado.
# No fim mostra quantos números foram digitados e a soma entre eles

soma = contador = 0

while True:
    num = int(input('Escreva um número inteiro: (0 para parar o programa) '))
    soma += num
    if num == 0:
        break
    contador += 1


print(f'\n\nForam digitados {contador} números.\n'
      f'A soma entre eles é {soma}')
