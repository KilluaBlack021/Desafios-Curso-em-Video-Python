# programa que conta quantos numeros foram digitados e só para quando apertar "enter"

coisa = ' '
c = soma = 0

while coisa != "":
    coisa = str(input('Escreva um número inteiro: ')).strip()
    if coisa.isnumeric():
        soma += int(coisa)
        c += 1

print(f'''
Você escreveu {c} números
A soma entre eles é {soma}
''')
