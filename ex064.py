'''
Exercício 64 - Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos foram digitados e qual foi a
soma entre eles(desconsiderando o flag).
'''

contador = 0
soma = 0
while True:
    n = int(input('\nDigite um número [para sair digite 999): '))
    contador += 1
    if n != 999:
        soma += n
    else:
        break
print('A soma dos {} números digitados é igual a {}.'.format(contador, soma))

