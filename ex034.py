'''
Exercício 034 - Escreva um programa que pergunte o salário de
um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual é o seu salário? R$'))

if salario  > 1250:
    novo = salario*1.1
else:
   novo = salario*1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))