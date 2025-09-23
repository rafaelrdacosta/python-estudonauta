'''
Exercício 55 - Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi maior e o menor peso lidos.
'''

maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}º pessoa: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso são {:.1f}kg'.format(maior))
print('O menor peso são {:.1f}kg'.format(menor))