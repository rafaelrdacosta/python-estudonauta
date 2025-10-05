'''
Exercício 084 - Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
a - Quantas pessoas foram cadastradas.
b - Uma listagem com as pessoas mais pesadas.
c - Uma listagem com as pessoas mais leves.
'''

dados = list()
pessoas = list()
maior = menor = 0
while True:
    nome = str(input('Nome: ')).strip()
    dados.append(nome)
    while True:
        peso = float(input('Peso: '))
        if peso <= 0:
            print('<ERRO> Opção inválida! Digite um peso maior que zero.')
        else:
            break
    dados.append(peso)

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'NS':
            break
        else:
            print('<ERRO> Opção inválida! Digite S ou N.')
    if opcao == 'N':
        break

print('-='*25)
print(pessoas)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoa(s).')
print(f'O maior peso foi de {maior:.2f}Kg. Peso(s) de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor:.2f}Kg. Peso(s) de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

