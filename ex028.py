'''
Exercício 028 - Escreva um programa que faça o
computador 'pensar' em um número inteiro entre
0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário
venceu ou perdeu.
'''

from random import randint
from time import sleep

num = randint(0, 5)
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-='*30)

chute = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if chute == num:
    print('Parabéns!! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, chute))