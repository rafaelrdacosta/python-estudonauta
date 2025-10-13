'''
Exercício 113 - Reescreva a função leiaInt() que fizemos no excercício 104,
incluinod agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(string):
    while True:
        try:
            num = str(input(f'{string} ')).strip()
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            try:
                num_int = int(num)
            except ValueError:
                print('\033[0;31m<ERRO> Por favor, digite um número inteiro válido!\033[m')
            else:
                return num_int

def leiaFloat(string):
    while True:
        try:
            num = str(input(f'{string} ')).strip().replace(',', '.')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0.0
        else:
            try:
                num_float = float(num)
            except ValueError:
                print('\033[0;31m<ERRO> Por favor, digite um número real válido!\033[m')
            else:
                return num_float

#Progrma principal
n = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O número inteiro digitado foi {n} e o real foi {f:.1f}')