'''
Aula 20 - Funções 1ª parte
'''

def lin():
    print('-' * 30)

def mensagem(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma A + B = {soma}')

def contador(*num):
    # (*) vai imprimir uma tupla com os argumentos passados
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

def soma_lista(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
#Progama principal
lin()
print('   CURSO EM VÍDEO   ')
print('   APRENDA PYTHON   ')
print('   GUSTAVO GUANABARA   ')
lin()

mensagem('SISTEMA DE ALUNOS')

soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

soma_lista(2,9, 4)