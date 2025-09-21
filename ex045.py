'''
Exercício 045 - Crie um programa que faça o computador jogar
Jokenpô com você (pedra, papel e tesoura).
'''

from random import choice
from emoji import emojize
from time import sleep

list = ['pedra', 'papel', 'tesoura']
computador = choice(list)

print('{:=^40}'.format(' Vamos jogar JOKENPÔ!! '))

jogador = str(input('''
Suas opções:
PEDRA
PAPEL
TESOURA
Qual é a sua jogada? ''')).lower()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=-'*8)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=-'*8)


if computador == 'pedra':
    if jogador == 'tesoura':
        print(emojize('Computador ganhou!\nPedra quebra Tesoura! ✊🏼'))
    if jogador == 'papel':
        print(emojize('Você ganhou!\nPapel embrulha Pedra! ✋'))
    if jogador == 'pedra':
        print('EMPATE! Jogue novamente!')
if computador == 'tesoura':
    if jogador == 'pedra':
        print(emojize('Você ganhou!\nPedra quebra Tesoura! ✊🏼'))
    if jogador == 'papel':
        print(emojize('Computador ganhou!\nTesoura corta Papel! ✌️'))
    if jogador == 'tesoura':
        print('EMPATE! Jogue novamente!')
if computador == 'papel':
    if jogador == 'tesoura':
        print(emojize('Você ganhou!\nTesoura corta Papel! ✌️'))
    if jogador == 'pedra':
        print(emojize('Computador ganhou!\nPapel embrulha Pedra! ✋'))
    if jogador == 'papel':
        print('EMPATE! Jogue novamente!')





