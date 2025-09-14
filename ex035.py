'''
Exercício 035 - Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
'''

print('-=-'*10)
print('Analisador de triângulos')
print('-=-'*10)

r1 = float(input('Digite o tamanho da 1ª reta: '))
r2 = float(input('Digite o tamanho da 2ª reta: '))
r3 = float(input('Digite o tamanho da 3ª reta: '))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas NÃO podem formar um triângulo.')