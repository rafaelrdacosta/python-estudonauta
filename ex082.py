'''
Exercício 082 - Crie um programa que vai ler vários números e colocar em uma
lista.
Depois disso, crie duas listas extras que vão contar apenas com valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    numeros.sort()

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('Opção inválida! Digite S ou N.')
    if opcao == 'N':
        break
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
print('-='*25)
print(f'A lista completa é {numeros}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
