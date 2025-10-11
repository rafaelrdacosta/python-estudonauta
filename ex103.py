'''
Exercício 103 - faça um programa que tenha um função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
'''

def ficha(nome = '<desconhecido>', gols = 0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa principal
nome = str(input('Nome do Jogador: ')).strip()

try:
    gols = input('Número de Gols: ')
    if gols.strip() == '':
        gols = 0
    else:
        gols = int(gols)
except ValueError:
    # Caso o usuário digite um texto que não é número
    print("Entrada de Gols inválida. Assumindo 0 gols.")
    gols = 0

ficha(nome, gols)