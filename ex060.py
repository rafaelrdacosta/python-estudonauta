'''
Exercício 060 - Faça um programa que leia um
número qualquer e mostre o seu fatorial.
5! = 5*4*3*2*1 = 120
'''

num = int(input('Digite um número: '))

'''fatorial = num
for c in range(num, 1, -1):
    fatorial = fatorial * (c - 1)
print('O fatorial de {} é igual a {}.'.format(num, fatorial))'''

fatorial = num
c = num
while c > 1:
    fatorial = fatorial * (c - 1)
    c -= 1
print('O fatorial de {} é igual a {}.'.format(num, fatorial))



