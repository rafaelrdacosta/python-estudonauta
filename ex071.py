'''
Exercício 071 - Crie um programa que simule o
funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão
entregues.

Obs: Considere que o caixa possui cédulas de
R$50, R$20, R$10 e R$1.
'''

print('='*35)
print('{:^35}'.format('BANCO CEV'))
print('='*35)

while True:
    saque = int(input('Que valor você quer sacar? R$ '))

    if saque < 10:
        qtd_um = saque
        print(f'Total de {qtd} cédulas de R$ 1.00')
    elif saque < 20:
        qtd_dez = saque // 10
        print(f'Total de {qtd_dez} cédula(s) de R$ 10.00')
        if saque % 10 != 0:
            qtd_um = saque % 10
            print(f'Total de {qtd_um} cédula(s) de R$ 1.00')
    elif saque < 50:
        if saque % 20 != 0:
            qtd_vinte = saque // 20
            print(f'Total de {qtd_vinte} cédula(s) de R$ 20.00')
        if saque % 10 != 0:
            qtd_um = saque % 10
            print(f'Total de {qtd_um} cédula(s) de R$ 1.00')
    else:
        qtd_cinquenta = saque // 50
        print(f'Total de {qtd_cinquenta} cédula(s) de R$ 50.00')
        if saque % 50 != 0:
            resto = saque % 50
            if resto % 20 == 0:
                qtd_vinte = resto // 20
                print(f'Total de {qtd_vinte} cédula(s) de R$ 20.00')
            else:
                qtd_vinte = resto // 20
                print(f'Total de {qtd_vinte} cédula(s) de R$ 20.00')
                qtd_dez = resto // 20
                print(f'Total de {qtd_dez} cédula(s) de R$ 10.00')

        if saque % 10 != 0:
                qtd_um = saque % 10
                print(f'Total de {qtd_um} cédula(s) de R$ 1.00')
    print('=' * 35)
    break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
