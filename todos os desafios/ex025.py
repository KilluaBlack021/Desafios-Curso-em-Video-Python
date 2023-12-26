# programa que le o nome de uma pessoa e diz se ela possui "silva" no nome

nome = str(input('Escreva seu nome: ')).strip()
n = nome.split()

if "silva" in nome.lower():
    print(f'Você {n[0]} tem "silva" no nome!')
else:
    print(f'{n[0]}, você não tem "silva" em seu nome!')
