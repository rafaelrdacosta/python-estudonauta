'''
Exercício 098 - Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a - de 1 até 10, de 1 em 1
b - de 10 até 0, de 2 em 2
c - uma contagem personalizada
'''

from time import sleep

def linha():
    print('-='*25)

def contagem_personalizada(inicio, fim, passo):
    if passo < 0:
        passo *= (-1)
    elif passo == 0:
        print('Será considerado o passo igual a 1.')
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            sleep(0.5)
        print('FIM!')
    elif inicio > fim:
        for i in range(inicio, fim - 1, passo*(-1)):
            print(f'{i} ', end='')
            sleep(0.5)
        print('FIM!')

def contador():
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!')
    linha()

    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i} ', end='')
        sleep(1)
    print('FIM!')
    linha()

    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    linha()
    contagem_personalizada(inicio, fim, passo)


#Programa principal
contador()