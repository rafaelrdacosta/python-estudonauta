'''
Exercício 012 - Faça um algoritimo que leia o preço
de um  produto e mostre seu novo preço com 5% de
desconto.
'''

preco = float(input('\nQual o preço do produto? R$'))
print('Preço com desconto - R${:.2f}'.format(preco*0.95))