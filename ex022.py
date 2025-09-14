'''
Exercício 22 - Crie um programa que leia o nome completo
de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todos sem considerar espaços.
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

lista = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(lista[0], len(lista[0])))