'''
Exercício 073 - Crie uma tupla preenchida com os 20
primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a - apenas os cinco primeiro colocados.
b - Os últimos 4 colocados.
c - uma lista com os times em ordem alfabética.
d - em que posição está o time da Chapecoense.
'''

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamento', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
          'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-='*15)
print('Lista de times do Brasileirão:')
for c in range(0, len(times)):
    print(times[c])
print('-='*15)
print('Os cinco primeiros são: ')
print(times[0:5])
print('-='*15)
print('Os 4 últimos são:')
print(times[-4:])
print('-='*15)
print('Times em ordem alfabética:')
print(sorted(times))
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição no campeonato.')