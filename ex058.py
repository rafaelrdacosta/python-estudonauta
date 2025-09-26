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
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-='*30)

acertou = False
palpite = 0
while not acertou:
    chute = int(input('Em que número eu pensei? '))
    palpite += 1
    print('PROCESSANDO...')
    sleep(1)

    if chute > num:
        print('Menos... Tente mais uma vez!')
    elif chute < num:
        print('Mais... Tente mais uma vez!')
    else:
        print('Parabéns!! Você conseguiu vencer!')
        acertou = True

print('Foram {} tentativa(s) até acertar!'.format(palpite))