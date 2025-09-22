'''
Exercício 051 - Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
'''

t = int(input('Digite o 1º termo da Progressão Aritmética: '))
r = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    print(t, end=' ')
    t += r