# A partir da quantia presente em sua carteira, direi quantos dolares você poderá comprar

saldo = float(input('Quantos reais você possui na carteira: '))

print(f'''Com R${saldo:.2f} na carteira, você pode comprar ${saldo/4.9:.2f} dólares.

Tchau!!! ''')
