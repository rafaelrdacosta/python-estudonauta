'''
Exercício 072 - Crie um programa que tenha uma
tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
'''

indices = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {indices[num]}.')
    else:
        continue

    opcao = '-'
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break


