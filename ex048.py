'''
Exercício 048 - Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        #print(c, end=' ')
        soma += c
print('\nA soma dos números ímpares múltiplos de três entre 1 e 500 é: {}'.format(soma))