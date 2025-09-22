'''
Exercício 036 - Escreva um programa para aprovar o
empréstimo bancário para a compra de uma casa. O
programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o
empréstimo será negado.
'''

valor = float(input('\nQual valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Quer financiar em quantos anos? '))

prestacao = valor / (anos*12)
max = salario * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, prestacao))

if prestacao > max:
    print('O financiamento não será liberado!')
else:
    print('Financiamento liberado!')


