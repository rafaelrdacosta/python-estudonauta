'''
Exercício 099 - Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros. Seu programa tem que analisar todos os
valores e dizer qual deles é o maior.
'''

from time import sleep

def linha():
    print('-=' * 20)

def maior(*valores):
    linha()
    print('Analisando os valores passados...')
    maior = cont = 0
    for num in valores:
        print(num, end=' ')
        sleep(0.5)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
    print(f'\nForam informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Pograma principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
