'''
Exercício 66 - Crie um programa que leia vários números
inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor
999, que a condição de parada.
No final mostre quantos números foram digitados e qual
foi a soma entre eles desconsiderando o 999.
'''

contador = 0
soma = 0
while True:
    num = int(input('\nDigite um valor (999 para parar): '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'A soma dos três {contador} valores foi {soma}!')
