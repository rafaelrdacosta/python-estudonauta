'''
Exercício 051 - Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
'''

t = int(input('\nDigite o 1º termo da Progressão Aritmética: '))
r = int(input('Digite a razão da PA: '))

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
print('Primeiro termo: {}'.format(t))
print('Razão: {}'.format(r))
for c in range(1, 11):
    print(t, end=' ')
    t += r


