'''
Exercício 096 - Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular(largura e comprimento) e mostre a área do
terreno.
'''

def cabecalho(titulo):
    print('-' * 30)
    print(f'{titulo:^30}')
    print('-' * 30)

def area(largura, comprimento):
    a = largura *comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


#Programa principal
cabecalho('Controle de Terrenos')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)


