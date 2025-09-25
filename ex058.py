'''
Exercício 058 - Melhore o jogo do Exercício 28, onde o computador vai pensar
em um número de 0 a 10. Só que agora o jogador vai tentar
advinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint
from time import sleep

num = randint(0, 10)
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-='*30)

palpite = 0
while True:
    chute = int(input('Em que número eu pensei? '))
    palpite += 1
    print('PROCESSANDO...')
    sleep(1)

    if chute == num:
        print('Parabéns!! Você conseguiu vencer!')
        break
    else:
        print('GANHEI! Tente novamente!')

print('Foram {} tentativa(s) até acertar!'.format(palpite))