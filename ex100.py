'''
Exercício 100 - Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.
'''

from random import randint

def sorteia():
    numeros = list()
    print(f'Sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5):
        num = (randint(1, 10))
        numeros.append(num)
        print(num, end=' ')
    print('PRONTO!')
    return numeros

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')


#Programa principal
lista = sorteia()
somaPar(lista)