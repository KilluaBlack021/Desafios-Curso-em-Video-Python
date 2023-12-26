# programa que lê um nome completo de alguem, mostrando logo depois o primeiro e o ultimo nome

nome = str(input('Escreva seu nome completo: ')).strip()
n = nome.split()

print(f'''
Seu nome completo é {nome}
O primeiro nome é {n[0]}
Seu ultimo nome é {n[-1]}

Tchau!!!''')
