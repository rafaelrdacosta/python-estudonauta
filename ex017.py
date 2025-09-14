'''
Exercício 017 - Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt, pow, hypot

cat1 = float(input('Qual comprimento do cateto oposto:'))
cat2 = float(input('Qual comprimento do cateto adjacente:'))
#hip = (cat1**2 + cat2**2)**0.5
#hip = sqrt(pow(cat1, 2) + pow(cat2, 2))
hip = hypot(cat1, cat2)
print('A hipotenusa do triângulo é {:.1f}'.format(hip))