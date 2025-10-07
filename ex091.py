'''
Exercício 091 - Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.
'''

from random import randint
from time import sleep

jogadores = ['jogador1', 'jogador2', 'jogador3', 'jogador4']
jogadas = {}
print('Valores sorteados:')
for nome in jogadores:
    num = randint(1, 6)
    jogadas[nome] = num
    print(f'O {nome} tirou {jogadas[nome]}')

print(jogadas)
jogadas_ordenadas = sorted(jogadas.items(), key=lambda item: item[1])
print('Ranking dos jogadores:')
print(jogadas_ordenadas)
for i in range(0, 4):
    print(f'{i}º lugar: {jogadas_ordenadas[i][0]} com {jogadas_ordenadas[i][1]}')