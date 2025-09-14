'''
Aula 008 - Utilizando módulos
'''

import math
from math import sqrt, floor
import random
import emoji

num = int(input('Digite um número:'))
raiz = math.sqrt(num) #utilizando import math
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))

raiz = sqrt(num) #utilizando from math import sqrt
print('A raiz quadrada de {} é igual a {:.1f}'.format(num, raiz))
print('A raiz quadrada de {} é igual a {}'.format(num, floor(raiz)))

numero = random.random() #o método random da classe random gera um número aleatório entre 0 e 1 (float)
print(numero)

num1 = random.randint(1, 10) #gera um número inteiro dentro do range passado como arguemnto
print(num1)

print(emoji.emojize('Olá, mundo!🌎'))

