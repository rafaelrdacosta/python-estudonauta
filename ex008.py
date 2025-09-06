'''
Exercício 008 - Escreva um programa que leia um
valor em metros e o exiba convertido em km, hm,
dam, dm, cm e mm.
'''

metros = float(input('\nDigite o valor em metros a ser convertido: '))
print('A medidade {:.1f}m corresponde a:'.format(metros))
print(f'{metros/1000}Km')
print(f'{metros/100}hm')
print(f'{metros/10}dam')
print(f'{metros*10}dm')
print(f'{metros*100}cm')
print(f'{metros*1000}mm')
