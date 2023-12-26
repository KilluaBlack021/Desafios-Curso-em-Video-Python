# programa que tem uma tupla com um monte de palavra sem acento
# para cada palavra, é pra mostra a sua respectiva vogal

palavras_sem_acentos = ('carro', 'cachorro', 'gato', 'python', 'programacao', 'computador', 'desenvolvimento', 'codigo',
                        'linguagem', 'inteligencia', 'artificial')

print('='*46)

for c in range(0, len(palavras_sem_acentos)):
    palavra = str(palavras_sem_acentos[c])
    na = 'a' if palavra.count('a') != 0 else '.'
    ne = 'e' if palavra.count('e') != 0 else '.'
    ni = 'i' if palavra.count('i') != 0 else '.'
    no = 'o' if palavra.count('o') != 0 else '.'
    nu = 'u' if palavra.count('u') != 0 else '.'

    print(f'{palavras_sem_acentos[c]:^20} tem as vogais: ', na, ne, ni, no, nu)

print('='*46)
