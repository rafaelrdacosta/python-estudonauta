'''
Exercício 101 - Crie um programa que tenha um função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas
eleições.
'''


def voto(ano_nasc):
    from datetime import datetime  #economiza memória importando localmente
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        resposta = 'NÃO VOTA.'

    elif 16 <= idade < 18  or idade > 65:
        resposta = 'VOTO OPCIONAL.'
    else:
        resposta = 'VOTO OBRIGATÓRIO.'

    return f'Com {idade} anos: {resposta}'


#Programa principal
print('-' * 30)
ano_nascimento = int(input('Em que  ano você nasceu? '))
print(voto(ano_nascimento))