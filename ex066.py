'''
Exercício 66 - Crie um programa que leia vários números
inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor
999, que a condição de parada.
No final mostre quantos números foram digitados e qual
foi a soma entre eles desconsiderando o 999.
'''

soma = contador = 0
while True:
    num = int(input('\nDigite um valor (999 para parar): '))
    if num == 999: #antes de realizar a contagem e soma pois 999 é uma flag
        break
    contador += 1
    soma += num

print(f'A soma dos {contador} valores foi {soma}!')
