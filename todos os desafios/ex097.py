# programa que tenha a função escreva(), ela recebe um texto como parametro e mostra uma msg com tamanho adaptavel

def escreva(txt):
    tamanho = len(txt) + 4
    linha = '=' * tamanho
    print(f'''{linha}
{txt:^{tamanho}}
{linha}''')


titulo = str(input('Escreva um texto curto: '))
escreva(titulo)
