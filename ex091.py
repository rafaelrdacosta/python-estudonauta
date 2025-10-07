'''
Exercício 091 - Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.
'''

from random import randint
from time import sleep

from PIL.DdsImagePlugin import item1

jogadas = dict()
print('Valores sorteados:')
for k, v in items():
    num = randint(1, 6)
    jogadas[c] = num
    print(f'O jogador {c+1} tirou {num}')
jogadas_ordenadas = sorted(jogadas.items(), key=lambda item: item[1])
print('Ranking dos jogadores:')
