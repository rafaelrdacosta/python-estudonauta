'''
Exercício 046 - Faça um programa que mostre na tela
a contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
from emoji import emojize

print('-='*14)
print('Contagem regressiva...')
for c in range(10, 0, -1):
    print(c, '...')
    sleep(1)
print(emojize('Feliz Ano Novo!!! 🎆 🎆 🎆'))
print('-='*14)