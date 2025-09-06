'''
Exercício 006 - Crie um algoritmo que leia um número
e mostre seu dobro, triplo e raiz quadrada.
'''

num = int(input('\nDigite um número: '))
print(f'Dobro de {num} é {num*2}.')
print(f'O triplo de {num} é {num*3}.')
print('A raiz quadrada de {} é {:.2f}'.format(num, (num**0.5)))