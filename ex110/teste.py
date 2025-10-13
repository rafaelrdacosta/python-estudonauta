'''
Exercício 110 - Adcione ao módulo moeda.py criado nos exercícios anteriores, uma
função chamada resumo(), que mostre na tela alguamas informações geradas pelas
funções que já temos no módulo criado até aqui.
'''

from ex110 import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 12)