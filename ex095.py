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
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('<ERRO> Opção inválida!!! Digite S ou N.')
    if opcao == 'N':
        break
print(lista_atletas)
print('-='*30)
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":>6}')
print('-'*43)
cont = 1
for i, atleta in enumerate(lista_atletas):
    print(f'{i + 1:<3} {atleta["nome"]:<15} {str(atleta["gols"]):<15} {atleta["total"]:>6}')
print('-'*43)

while True:
    nr_jogador = int(input('Mostrar dados de qual jogador? (Digite 999 para sair) '))
    if nr_jogador == 999:
        break

    indice_jogador = nr_jogador - 1
    if 0 <= indice_jogador < len(lista_atletas):
        jogador = lista_atletas[indice_jogador]

        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"].upper()}:')
        for i, gols in enumerate(jogador['gols']):
            print(f'No jogo {i + 1} fez {gols} gol(s).')
        print(f'total de gols: {jogador["total"]}')
    else:
        print(f'<ERRO> Não existe jogador com o código {nr_jogador}.')
print('<< VOLTE SEMPRE >>')