'''
Exercício 079 - Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []
while True:
    n = int(input('Digite um valor: '))

    if n in lista:
        print('Valor duplicado! Não vou adcionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('Opção inválida! Digite S ou N.')
    if opcao == 'N':
        break
print('-=' * 25)
lista.sort()
print(f'Você digitou os valores {lista}')
