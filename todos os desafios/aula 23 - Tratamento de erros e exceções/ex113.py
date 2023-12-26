# reescreva a função leia_int() feito no ex104, incluindo possibilidade de digitação de um número de tipo inválido.
# aproveite e crie também uma função de leia_float() com mesma funcionalidade.


def leia_int():
    while True:
        num = input('Escreva um número inteiro: ').strip()
        try:
            return int(num)
        except (ValueError, TypeError):
            if num == '':
                print(f'\033[33mNenhum valor foi digitado pelo usuario. Considerando valor "0".\033[m')
                return 0
            print(f'\033[31mO valor "{num}" não é um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario.\033[m')


def leia_float():
    while True:
        num = input('Escreva um número real: ').strip()
        try:
            return float(num)
        except ValueError:
            if num == '':
                print(f'\033[33mNenhum valor foi digitado pelo usuario. Considerando valor "0".\033[m')
                return 0
            print(f'\033[31mERRO: O valor "{num}" não é um número real.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario.\033[m')


# numero = leia_int()
numero_int = leia_int()
numero_float = leia_float()
print(f'''

Você digitou o número inteiro: {numero_int}
Você digitou o número real: {numero_float}
''')
