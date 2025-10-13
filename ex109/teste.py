'''
Exercício 109 - Modifique as funções que foram criadas no exercício 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai
ser ou não formatado pela função moeda(), desenvolvida no exercício 108.
'''

from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, False)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}.')