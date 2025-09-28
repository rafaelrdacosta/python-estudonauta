'''
 Exercício 076 - Crie um programa que tenha um tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados de forma tabular.
'''

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for pos, item in enumerate(lista):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7}')
print('-'*40)