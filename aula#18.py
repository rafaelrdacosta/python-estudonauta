'''
Listas compostas
'''

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera.append(['Rafael', 44])
print(galera)

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(p)

for p in pessoas:
    print(f'{p[0]} ten {p[1]} anos de idade.')

alunos = list()
dados = list()
totmen = totmai = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    alunos.append(dados[:])
    dados.clear()
print(alunos)

for aluno in alunos:
    if aluno[1] >= 21:
        print(f'{aluno[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{aluno[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
