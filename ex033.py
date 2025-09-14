'''
Exercício 033 - Faça um programa que leia
três números e mostre qual é o maior e qual é
menor.
'''

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1
if n2 < n1:
    menor = n2
if n3 < n2:
    menor = n3

print('\nO maior é o número {}!'.format(maior))
print('O menor é o número {}!'.format(menor))

