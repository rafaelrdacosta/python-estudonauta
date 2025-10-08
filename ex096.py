'''
Exercício 096 - Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular(largura e comprimento) e mostre a área do
terreno.
'''

def area(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura *comprimento}m².')

print('-'*30)
print(f'{'Controle de Terrenos':^30}')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)


