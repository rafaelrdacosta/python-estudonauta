'''
Exercício 039 - Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
'''

from datetime import date

ano = int(input('Em que ano você nasceu? '))
sexo = str(input('Qual seu sexo[masculino ou feminino]? ')).lower()
ano_atual = date.today().year
idade = ano_atual - ano

if sexo == 'masculino':
    print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, ano_atual))

    if idade == 18:
        print('Apresente-se a Junta do Serviço Militar de seu município.')
    elif idade < 18:
        tempo = 18 - idade
        print('Ainda faltam {} ano(s) para o alistamento.'.format(tempo))
        print('Seu alistamento será em {}.'.format(ano_atual + tempo))
    else:
        tempo = idade - 18
        print('Você já deveria ter se alistado há {} ano(s).'.format(tempo))
        print('Seu alistamento foi em {}.'.format(ano_atual - tempo))
else:
    print('O alistamento não é obrigatório para o sexo feminino.')