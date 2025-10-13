'''
Exercício 104 - Crie um programa que tenha uma função leiaint(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a validação para
aceitar apenas um valor numérico.
Ex:
n = leiaint('Digite um n')
'''

def leiaInt(string):
    valido = False
    while not valido:
        num = str(input(f'{string}'))
        try:
            valor = int(num)
            valido = True
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor


#Programa principal
print('-' * 30)
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')