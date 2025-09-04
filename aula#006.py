'''
Aula #006 - Tripos primitivos e saída de dados
'''

n1 = input('Digite um valor: ')
print(type(n1))

n2 = int(input('Digite um valor: '))
print(type(n2))

n3 = int(input('Digite um valor: '))
n4 = int(input('Digite outro valor: '))
soma = n3 + n4
print(f'A soma entre {n3} e {n4} vale {soma}.')
print('A soma entre {} e {} vale {}.'.format(n3, n4, soma))

n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isupper())