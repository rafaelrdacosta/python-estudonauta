'''
Exercício 065 - Crie um programa que leia vários
números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar mais valores.
'''

contador = 0
soma = 0
media = 0
while True:
    n = int(input('\nDigite um número inteiro: '))
    contador += 1
    soma += n
    media = soma / contador

    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    opcao = str(input('Deseja continuar [S/N]: ')).upper()
    if opcao == 'S':
        continue
    else:
        break

print('O foram digitados {} números e a média entre eles é {:.2f}.'.format(contador, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))