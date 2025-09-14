'''
Exercício 022 - Crie um programa que leia o nome
de uma cidade e diga se ela começa ou não como
o nome 'SANTO'.
'''

cidade = str(input('Em que cidade você nasceu:')).strip()
#cidade = cidade.upper().split()
#print(cidade)
#print('SANTO' == cidade[0])

print(cidade[:5].upper() == 'SANTO')