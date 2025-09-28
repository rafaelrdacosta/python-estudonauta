'''
Exercício 067 - Faça um programa que mostre a tabuada
de vários números, um de cada vez, para cada valor
digitado pelo usuário, o programa será interrompido
quando o número solicitado for negativo.
'''


while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
        print(f'{num} * {c:2} = {num*c:4}')
    print('-' * 40)

print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')