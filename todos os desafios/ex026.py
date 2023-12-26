# programa que conta o numero de letras "a" em uma string, fala a posição da primeria e da ultima ocorrencia

frase = str(input('Escreva uma frase: ')).strip().lower()

print(f'''
O número de letras "a" presente em sua frase é {frase.count('a')}
A posição da primeira letra "a" é {frase.find('a') + 1}
A posição da ultima letra "a" é {frase.rfind('a') + 1}

Tchau!!!''')
