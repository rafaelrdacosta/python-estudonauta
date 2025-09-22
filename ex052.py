'''
Exercício 052 - Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

primo = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, (n // 2 + 1)):
    if n % c == 0:
        primo += 1
if primo == 1:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))