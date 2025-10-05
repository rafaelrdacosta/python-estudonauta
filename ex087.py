'''
Exercício 087 - Aprimore o desafio anterior, mostrando no final:
a - a soma de todos os valores pares digitados.
b - a soma dos valores da terceira coluna
c - o maior valor da segunda linha
'''

linha = list()
matriz = list()
soma_pares = soma_col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        linha.append(num)
    matriz.append(linha[:])
    linha.clear()
print('-='*15)
for l in range(0, 3):
    soma_col += matriz[l][2]
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_col}.')
print(f'O maior valor da segunda linha é {maior}.')