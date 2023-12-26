# programa que le o sexo de alguem mas so aceite "M" ou "F", caso esteja errado, faça-o digitar novamente corretamente

s = ''

while s != "M" and "F":
    s = str(input('\n\nQual o seu sexo? \n\n     [M]masculino ou [F]feminino\n\n R: ')).strip().upper()
