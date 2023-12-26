# Este programa é um conversor de temperatura entre graus Cº e Fº

def linha(tipo):
    if tipo == 1:
        print('-'*60)
    elif tipo == 2:
        print('-='*30)


# boas-vindas
linha(2)
print(f'{"ESTE É UM CONVERSOR DE TEMPERATURA!":^60}')
linha(2)
# principal
while True:
    tenho = queroSaber = ''
    tipoDeConversao = int(input(f'''{"Qual o tipo de conversão que você deseja fazer?":^60}
 
[1]Celsius -> Fahrenheit 
[2]Fahrenheit -> Celsius

R:'''))
    linha(1)
    if tipoDeConversao == 1:
        tenho = "Celsius"
        queroSaber = "Fahrenheit"
    elif tipoDeConversao == 2:
        tenho = "Fahrenheit"
        queroSaber = "Celsius"
    graus = float(input(f'''{f"Para saber quantos graus {tenho} são em {queroSaber}.":^60}
    
Escreva o valor de graus {tenho}:

 R:'''))
    linha(1)
    if tenho == "Celsius":
        print(f'{f"{graus}Cº são aproximadamente {graus * 1.8 + 32:.2f}Fº":^60}')
    elif tenho == "Fahrenheit":
        print(f'{f"{graus}Fº são aproximadamente {(graus - 32) / 1.8:.2f}Cº":^60}')
    linha(1)
    # conversao
    repeticao = str(input(f'{"Quer continuar?  [S/s]Sim   [N/n]Não":^60}'))
    while repeticao not in "SNsn":
        linha(1)
        repeticao = str(input(f'{"!!!NÃO ENTENDI!!!":^60} \n{"Quer continuar?  [S/s]Sim   [N/n]Não":^60}\n R:'))
    if repeticao in 'Nn':
        break

print('Tchau!!!')
