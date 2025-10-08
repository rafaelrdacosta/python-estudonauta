'''
Exercício 093 - Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o
campeonato.
'''

ficha_atleta = dict()
ficha_atleta['nome'] = str(input('Nome do jogador: '))
while True:
    qtd_partidas = int(input(f'Quantas partidas {ficha_atleta['nome']} jogou? '))
    if qtd_partidas > 0:
        break
    else:
        print('<ERRO> Valor inválido!!! Digite uma quantidade maior que 0.')
gols_partida = list()
soma = 0
for i in range(1, qtd_partidas + 1):
    gols = int(input(f' Quantos gols na partida {i}? '))
    gols_partida.append(gols)
    soma += gols
ficha_atleta['gols'] = gols_partida
ficha_atleta['total'] = soma
print('-='*30)
print(ficha_atleta)
print('-='*30)
for k, v in ficha_atleta.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {ficha_atleta['nome']} jogou {qtd_partidas} partidas.')
for i, gols in enumerate(gols_partida):
    print(f'=> Na partida {i + 1}, fez {gols} gols.')
print(f'Foi um total de {soma} gols.')