'''
Exercício 010 - Crie um programa que leia quanto
dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.
US$1.00 = R$3.27
'''

real = float(input('\nQuanto dinheiro você tem? R$'))
dolar = real/3.27
print('R${:.2f} equivale a U${:.2f}.'.format(real, dolar))

