'''
Exercício 068 - Faça um programa que jogue par ou
ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

contador = 0
while True:
    num = int(input('Digite um valor: '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    computador = randint(0, 10)
    soma = computador + num

    print(f'Você jogou {num} e o computador {computador}.')
    print(f'Total de {soma}.')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    print('-' * 30)

    if jogador == 'P':
        if soma % 2 == 0:
            contador += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break

    elif jogador == 'I':
        if soma % 2 == 0:
            print('Você PERDEU!')
            break
        else:
            contador += 1
            print('Você VENCEU!')
    print('Vamos jogar novamente!')
    print('=-' * 15)
    
print('=-' * 15)
print(f'GAME OVER! Você venceu {contador} vez(es).')
