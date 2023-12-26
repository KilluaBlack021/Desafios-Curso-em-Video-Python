# programa com a função leia_int() que funciona semelhantemente ao input(), mas fazendo uma validação, aceitando apenas
# valores numericos

def leia_int(num):
    if num.isnumeric():
        return num
    else:
        return f'\033[31m --- Valor invalido!!! ---\n \033[m \033[4m"{num}"\033[m não é um número.'


numero = leia_int('jhgghj')
print(numero)
