'''
Exercício 060 - Faça um programa que leia um
número qualquer e mostre o seu fatorial.
5! = 5*4*3*2*1 = 120
'''

from math import factorial

num = int(input('Digite um número para calcular o fatorial: '))

'''fatorial = num
for c in range(num, 1, -1):
    fatorial = fatorial * (c - 1)
print('O fatorial de {} é igual a {}.'.format(num, fatorial))

fatorial = factorial(num)'''

print('Calculando o fatorial de {}...'.format(num))
fatorial = 1
c = num
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end= ' ')
    fatorial *= (c)
    c -= 1

print('{}.'.format(fatorial))



