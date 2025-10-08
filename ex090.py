'''
Exercício 090 - Faça um programa que leia o nome e a média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na
tela.
'''

ficha = {}
nome = str(input('Nome: ')).strip()
ficha['Nome'] = nome
media = float(input(f'Média de {nome}: '))
ficha['Média'] = media
if media >= 7:
    ficha['Situação'] = 'Aprovado'
elif 5 <= media < 7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'

print('-='*30)
for k, v in ficha.items():
    print(f'{k} é igual a {v}.')