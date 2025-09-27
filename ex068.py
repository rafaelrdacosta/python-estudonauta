'''
Exercício 068 - Faça um programa que jogue par ou
ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
'''

from random import randint

computador = randint(0, 10)

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

contador = 0
while True:
    num = int(input('Digite um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    print('-' * 30)
    soma = computador + num

    print(f'Você jogou {num} e o computador {computador}.')
    print('-' * 30)

    if jogador in 'Pp':
        if soma % 2 == 0:
            contador += 1
            print(f'Total de {soma} DEU PAR.')
            print('Você VENCEU!\nVamos jogar novamente...')
        else:
            print(f'Total de {soma} DEU IMPAR.')
            print('Você PERDEU!')
            break

    elif jogador in 'Ii':
        if soma % 2 == 0:
            print(f'Total de {soma} DEU PAR.')
            print('Você PERDEU!')
            break
        else:
            contador += 1
            print(f'Total de {soma} DEU IMPAR.')
            print('Você VENCEU!\nVamos jogar novamente...')
    print('=-' * 15)
    
print('=-' * 15)
print(f'GAME OVER! Você venceu {contador} vezes.')
