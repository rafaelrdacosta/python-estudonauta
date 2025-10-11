'''
Exercício 104 - Crie um programa que tenha uma função leiaint(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a validação para
aceitar apenas um valor numérico.
Ex:
n = leiaint('Digite um n')
'''

def leiaint(string):
    num = str(input(f'{string}'))
    try:
        int(num)
    except ValueError:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = str(input(f'{string}'))



#Programa principal
print('-' * 30)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')