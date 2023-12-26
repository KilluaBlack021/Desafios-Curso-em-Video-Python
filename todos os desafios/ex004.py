# Você digita um valor e eu mostro caracteriscas sobre

algo = input('Digite algo: ')

print(f'"{algo}" é uma letra: {algo.isalpha()}')
print(f'"{algo}" é um número: {algo.isnumeric()}')
print(f'"{algo}" só tem letra maiuscula: {algo.isupper()}')
print(f'"{algo}" só tem letra minuscula: {algo.islower()}')
print(f'"{algo}" é decimal: {algo.isdecimal()}')
print(f'"{algo}" é uma digito: {algo.isdigit()}')
