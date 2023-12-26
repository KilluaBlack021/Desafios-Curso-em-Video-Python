# Este programa calculará o area de uma parede e mostrará quantos litros de tinta serão gastos. 2m²/L

largura = float(input('Largura da sua parede: '))
comprimento = float(input('Comprimento da parede: '))
area = largura * comprimento

print(f'\nSerão usados aproximadamente {area / 2:.2f}L de tinta para uma area de ~={area:.2f}m²\n\nTchau!!!')
