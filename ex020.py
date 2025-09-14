'''
Exercício 020 - O mesmo professor do desafio anterior
quer sortear a ordem de apresentação de trabalhos dos
alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a orem sorteada.
'''

from random import shuffle

n1 = str(input('1º Aluno:'))
n2 = str(input('2º Aluno:'))
n3 = str(input('3º Aluno:'))
n4 = str(input('4º Aluno:'))

lista = [n1, n2, n3, n4]
#Embaralhar a ordem da lista
shuffle(lista)

print('Ordem de apresentação do trabalho:\n{}.'.format(lista))