'''
Exercício 086 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

dados = list()
matriz = list()
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        dados.append(num)
    matriz.append(dados[:])
    dados.clear()
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^3} ]', end='')
    print()