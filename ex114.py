'''
Exercício 114 - Crie um código em Python que teste se o site Pudim está acessível
pelo computador usado.
'''

import requests

url = 'https://www.pudim.com.br'
try:
    response = requests.get(url)
except:
    print('\n\033[0;31mO site Pudim não está acessível no momento.')
else:
    print('\n\033[0;33mConsegui acessar o site Pudim com sucesso!')

