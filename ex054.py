'''
Exercício 054 - Crie um programa que leia o ano de
nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas
já são maiores.
'''

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento {}º pessoa: '.format(c+1)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoas já atingiram a maioridade.'.format(maior))
print('{} pessoas ainda são menores de idade.'.format(menor))



