'''
Exercício 023 - Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um dos digitos
separados.
'''

num = input('Digite um número (de 0 a 9999):')

print('''Como string:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'''.format(num[3], num[2], num[1], num[0] ))

num = int(num)
print('''\nComo inteiro:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'''.format(num%10, num%100//10, num%1000//100, num//1000))