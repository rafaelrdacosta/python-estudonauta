'''
Exercício 088 - Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from time import sleep
from random import sample

print('-'*40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:=^40}'.format(' SORTEANDO 4 JOGOS '))
aposta = list() #lista completa com os cincos volantes de apostas
volante = list()
for i in range(0, jogos):
    print(f'Jogo {i + 1}: ', end='')
    volante = sample(range(1, 60), 6)
    volante.sort()
    aposta.append(volante[:])
    print(volante)
    volante.clear()
    sleep(1)
print('{:=^40}'.format(' < BOA SORTE! > '))




