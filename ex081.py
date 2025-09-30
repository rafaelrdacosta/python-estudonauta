'''
Exercício 081 - Crie um programa que vai ler vários números e colocar em uma
lista.
'''

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    lista.sort(reverse=True)

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('Opção inválida! Digite S ou N.')
    if opcao == 'N':
        break
print('-='*25)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')

if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print(f'O valor 5 foi encontrado na lista na(s) posição(ões) ', end='')
    for c, n in enumerate(lista):
        if n == 5:
            print(c, end='')



