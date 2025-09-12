'''
Exercício 014 - Escreva um programa que converta uma temperatura
de ºC para ºF.
'''

celsius = float(input('Informe a temperatura em ºC:'))
fahrenheit = (celsius * 1.8) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(celsius, fahrenheit))
