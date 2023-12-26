# programa que lê varios números e coloca numa lista. Depois, mostre:
# quantos números foram digitados.
# A lista de valores ordenada de forma decrescente
# se o valor 5 foi digitado e está ou não na lista

numeros = []
cinco = ''

print('='*30)
while True:
    n = int(input('Escreva um número: '))
    numeros.append(n)

    continua = str(input('Quer continuar? [S/N]')).strip().upper()
    while continua not in 'SN':
        continua = str(input('Não entendi!!! Quer continuar? [S/N]')).strip().upper()
    if continua == "N":
        break


# if 5 in numeros:
#     cinco = 'ESTÁ NA LISTA!!!'
# else:
#     cinco = 'NÃO ESTÁ NA LISTA!!!'

print('='*30)
print(f'''A partir dos dados informados, infere-se que:

Valores digitados: {numeros}

valores organizados decrescentemente: {sorted(numeros, reverse=True)} 
Foram digitados {len(numeros)} numeros;
O número "5" {"está na lista!!!" if 5 in numeros else "não está na lista!!!"}
''')
