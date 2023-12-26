# programa que lê o nome completo de alguem e mostra  o nome dela com todas as letras minusculas,
# conta quantas letras tem (não conta espaços) e conta quantas letras tem o primeiro nome.

from time import sleep

nome = str(input('Escreva seu nome completo: ')).strip()
nomeSplit = nome.split(' ')
print('Analisando seu nome...')
sleep(1)
print(f'''\n \033[1m---{nome}---\033[m\n
Seu nome com todas a letras maiuscula é \033[1m{nome.upper()}\033[m
Seu nome em letras minusculas é \033[1m{nome.lower()}\033[m
Ele tem \033[1m{len(nome) - nome.count(' ')}\033[m letras no total 
Mas o primeiro nome tem \033[1m{len(nomeSplit[0])}\033[m letras.

Tchau!!!''')
