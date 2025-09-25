'''
Exercício 061 - Refaça o exercício 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
'''

t = int(input('\nDigite o 1º termo da Progressão Aritmética: '))
r = int(input('Digite a razão da PA: '))

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

print('Primeiro termo: {}'.format(t))
print('Razão: {}'.format(r))

c = 1
while c < 11:
    print(t, end=' ')
    t += r
    c += 1