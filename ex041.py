'''
Exercício 041 - A confederação Nacional de Natação
precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com
a idade:
- até 9 anos: Mirim
- até 14 anos: Infantil
- até 19 anos: Júnior
- até 20 anos: Sênior
- acima: master
'''

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nascimento

print('Idade: {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: Mirim'.format(idade))
elif idade <= 14:
    print('Categoria: Infantil'.format(idade))
elif idade <= 19:
    print('Categoria: Júnior'.format(idade))
elif idade <= 20:
    print('Categoria: Sênior'.format(idade))
else:
    print('Categoria: Master'.format(idade))