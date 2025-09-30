'''
Exercício 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista.
No final, mostre qual foi o maior e o menor valor digitado e os suas respectivas
posições na lista.
'''

lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para Posição {c}: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print('=-' * 25)
print(f'Você digitou os valore {lista}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, n in enumerate(lista):
    if n == maior:
        print(f'{c}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, n in enumerate(lista):
    if n == menor:
        print(f'{c}...', end='')








