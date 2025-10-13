'''
Exercício 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumenta(), diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções
'''

def aumentar(valor, porcentagem):
    resultado =  valor + (porcentagem/100 * valor)
    return resultado

def diminuir(valor, porcentagem):
    resultado = valor - (porcentagem/100 * valor)
    return resultado

def dobro(valor):
    resultado =  valor * 2
    return resultado

def metade(valor):
    resultado = valor / 2
    return resultado