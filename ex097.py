'''
Exercício 097 - Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.
Ex:
escreva('Olá, Mundo!')
Saída
-------------
 Olá, Mundo!
-------------
'''

def escreva(msg):
    tam = len(msg)
    print('~' * (tam+4))
    print(f'{msg:^{tam+4}}')
    print('~' * (tam + 4))


escreva('Gustavo Guanabara')
escreva('Curso em Python no Youtube')
escreva('Cev')