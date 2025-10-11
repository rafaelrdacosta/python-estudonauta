'''
Exercício 106 - Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
a palavra 'FIM', o programa se encerrará.
OBS: use cores.
'''

def cabecalho_pcp(msg):
    tam = len(msg) + 4
    print('\033[30:43m~' * (tam))
    print(f'{msg:^{tam}}')
    print('~' * (tam))
    print('\033[m')

def cabecalho_func(msg):
    tam = len(msg) + 4
    print('\033[30:44m~' * (tam))
    print(f'{msg:^{tam}}')
    print('~' * (tam))
    print('\033[m')

def my_help(string):
    msg = f"Acessando o manual do comando '{string}'"
    cabecalho_func(msg)
    print('\033[30:47m')
    help(string)
    print('\033[m')

#Programa principal
while True:
    cabecalho_pcp('SISTEMA DE AJUDA PyHELP')
    funcao = str(input('Função ou Biblioteca > ')).strip().lower()
    if funcao == 'fim':
        print('\033[30:45m~' * 20)
        print(f'{'ATÉ LOGO!':^20}')
        print('~' * 20)
        print('\033[m')
        break
    my_help(funcao)
