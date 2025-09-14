'''
Exercício 018 - Faça um programa que leia um ângulo
qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''

from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo que você deseja:'))
#Primeiro tem que converter o valor do ângulo de graus para radianos
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Para o ângulo {}:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(angulo, seno, cosseno, tangente))