# código que teste a conexão com algum site, mostrando se ele está ou não acessivel.

import requests

# site = 'https://www.facebook.com'
site = 'abobrinha.com.xampoo'

try:
    n_sei = requests.get(site)
    print(f'Conexão com o site {site} realizada com sucesso!')
except requests.exceptions.MissingSchema:
    print(f'\033[31mNão foi possivel efetuar a conexão com o site\033[m: {site}')
finally:
    print('\n\nBoa noite!!!')
