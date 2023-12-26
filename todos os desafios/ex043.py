# programa que calcula seu IMC e mostra seu status

status = ''
peso = float(input('Qual o seu peso? \nR: '))
altura = float(input(f'Qual sua altura (em cm)?  \nR: ')) / 100
imc = peso / (altura ** 2)


if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
elif imc > 40:
    status = 'Obesidade morbida'

print(f'Com base nos dados adquiridos, um IMC de {imc}, pode-se considerar que você tem "{status}".')
