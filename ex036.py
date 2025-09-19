'''
Exercício 036 - Escreva um programa para aprovar o
empréstimo bancário para a compra de uma casa. O
programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o
empréstimo será negado.
'''

valor = float(input('Qual valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Quer financiar em quantos anos? '))

prestacao = valor / (anos*12)
max = salario * 0.3

if prestacao > max:
    print('A prestação de R${:.2f} excede o limite de 30% de seu salário.\nO financiamento não será liberado!'.format(prestacao))
else:
    print('Financiamento liberado em {} anos com parcelas no valor de R${:.2f}'.format(anos, prestacao))


