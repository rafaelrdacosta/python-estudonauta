'''
Exercício 16 - Crie um programa que leia um número
real qualquer pelo teclado e mostre na tela a sua
porção inteira.
'''

from math import trunc

num = float(input('Digite um número real:'))
print('A parte inteira de {} é {}'.format(num, trunc(num)))
print('A parte inteira de {} é {}'.format(num, int(num))) #utilizando typecasting