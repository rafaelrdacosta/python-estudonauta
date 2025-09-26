'''
Exercício 065 - Crie um programa que leia vários
números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar mais valores.
'''

soma = contador = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('\nDigite um número inteiro: '))
    contador += 1
    soma += n

    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

media = soma / contador
print('Foram digitados {} números e a média entre eles é {:.2f}.'.format(contador, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))