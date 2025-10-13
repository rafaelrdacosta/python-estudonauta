'''
Exercício 108 - Adapte o código do exercício 107, criando uma função adcional
chamada moeda() que consiga mostrar os valores como um valor monetário.
'''

def aumentar(preco=0, porcentagem = 0):
    return preco + (porcentagem/100 * preco)


def diminuir(preco=0, porcentagem = 0):
    return preco - (porcentagem/100 * preco)


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0, moeda = 'R$'):
    return f'{moeda} {preco:>.2f}'.replace('.', ',')