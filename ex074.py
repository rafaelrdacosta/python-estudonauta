'''
Exercício 074 - Crie um programa que vai gerar cinco
números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão
na tupla.
'''

from random import randint

# Inicializamos a tupla vazia.
numeros = ()
maior = menor = 0
print('Os valores sorteados foram: ', end=' ')
for c in range(0, 5):
    n = randint(1, 10)
    #Concatenação: cria-se uma nova tupla que irá receber os novos Elm
    # A vírgula (n,) é crucial para que o Python trate 'n' como uma tupla de um único item.
    numeros += (n, )
    print(n, end=' ')
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')

#Funções max e min
#print(f'\nO maior valor sorteado foi {max(numeros)}.')
#print(f'O menor valor sorteado foi {min(numeros}.')

