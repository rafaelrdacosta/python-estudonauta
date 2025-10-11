'''
Exercício 102 - Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
'''

def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: o número que será calculado
    :param show: True ou False (opcional) mostra ou não a conta.
    :return: o valor fatorial de um número n
    '''
    fat = 1
    print('-' * 30)
    for i in range(num, 0, -1):
        if show == True:
            fat *= i
            print(f'{i} ', end='')
            if i != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        if show == False:
            fat *= i
    return fat


#Programa principal
help(fatorial)
print(fatorial(5, True))
print(fatorial(5, False))
print(fatorial(5))
