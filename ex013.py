'''
Exercício 013 -  Faça um algoritimo que leia o salário
de um funcionário e mostre seu novo salário, com 15%
de aumento.
'''

salario = float(input('\nQual é o seu salário? R$'))
print('Seu novo salário com aumento é de R${:.2f}.'.format(salario*1.15))