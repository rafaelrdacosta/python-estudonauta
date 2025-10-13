'''
Exercício 111 - Crie um pacote chamado utilidadeCev que tenha dois módulos
internos chamados moeda e dado.
Transfira todas as funções utilizadas nos exercícios 107, 108, 109 para o
primeiro pacote e mantenha tudo funcionando.
'''

from ex111.utilidadesCev import moeda

p = float(input('Digite o preço: '))
moeda.resumo(p, 35, 22)