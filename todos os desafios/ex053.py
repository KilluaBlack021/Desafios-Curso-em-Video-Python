# programa que lê uma frase e diz se ela é um palindromo ao desconciderar espaços

situacao = ''

# recebe a frase, tira espaços desnecessarios e transforma em lista
original = str(input('Escreva uma frase: ')).strip().upper()
frase = original.split()
# transforma em string novamente
string_de_frase = ''.join(frase)
inverso_de_frase = string_de_frase[::-1]

"""
# varre a sting de trás para frente enquanto cria uma lista invertida de "frase"
for i in range(len(string_de_frase) - 1, -1, -1):
    inverso_de_frase.append(string_de_frase[i])
"""

# transforma em string
string_inverso_frase = ''.join(inverso_de_frase)

# compara ambas as strings/ determina se é um PALIMDROMO ou não
if string_de_frase == string_inverso_frase:
    situacao = 'É'
else:
    situacao = 'NÂO É'


print(f'A frase: "{original}" que você digitou e "{string_inverso_frase}", {situacao} um PALINDROMO.')
