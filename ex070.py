'''
Exercício 070 - Crie um programa que leia o nome e o
preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a - Qual é o total gasto na compra.
b - Quantos produtos custam mais de R$ 1000.
c - Qual o nome do produto mais barato.
'''

print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

total = maior_mil = mais_barato = contador =  0
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))

    total += preco
    contador += 1

    if preco > 1000:
        maior_mil += 1

    if contador == 1:
        mais_barato = preco
        nome_mais_barato = nome
    elif preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome

    opcao = '-'
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('-' * 30)

print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {maior_mil} produto(s) custando mais de R$ 1000.00.')
print(f'O produto mais barato foi a(o) {nome_mais_barato} que custou R${mais_barato:.2f}.')