'''
Exercício 095 - Aprimore o exercício 093 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de
cada jogador.
'''

ficha_atleta = dict()
lista_atletas = list()
while True:
    print('-'*30)
    nome = str(input('Nome do jogador: '))
    ficha_atleta['nome'] = nome
    while True:
        qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
        if qtd_partidas > 0:
            break
        else:
            print('<ERRO> Valor inválido!!! Digite uma quantidade maior que 0.')
    gols_partida = list()
    soma = 0
    for i in range(1, qtd_partidas + 1):
        gols = int(input(f'Quantos gols na partida {i}: '))
        gols_partida.append(gols)
        soma += gols
    ficha_atleta['gols'] = gols_partida
    ficha_atleta['total'] = soma

    lista_atletas.append(ficha_atleta.copy())

    while True:
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('<ERRO> Opção inválida!!! Digite S ou N.')
    if opcao == 'N':
        break
print(lista_atletas)
print('-='*30)
print('cod ', end='')
for i in ficha_atleta.keys():
    print(f'{i:<15}', end='')
print()

print('-='*30)
for k, v in enumerate(lista_atletas):
    print(f'{k+1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
print(f'O jogador {nome} jogou {qtd_partidas}.')
for i, gols in enumerate(gols_partida):
    print(f'=> Na partida {i + 1}, fez {gols} gols.')
print(f'Foi um total de {soma} gols.')