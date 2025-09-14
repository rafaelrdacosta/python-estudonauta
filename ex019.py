'''
Exercício 019 - Um professor quer sortear um dos seus
quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome
do escolhido.
'''

from random import choice

n1 = str(input('1º Aluno:'))
n2 = str(input('2º Aluno:'))
n3 = str(input('3º Aluno:'))
n4 = str(input('4º Aluno:'))

sorteado = choice([n1, n2, n3, n4])

print('O aluno escolhido para apagar o quadro foi o {}'.format(sorteado))