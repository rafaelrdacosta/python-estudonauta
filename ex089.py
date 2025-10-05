'''
Exercício 089 - Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a
média de cada um e permita mostrar as notas de cada aluno individualmente.
'''

ficha = list() # Lista principal para guardar todos os registros

while True:
    registro = list()  # Lista temporária: [Nome, [Notas], Média]
    nome = str(input('Nome: ')).strip()
    registro.append(nome)

    notas = list()
    soma = 0
    for i in range(0, 2):
        while True:
            nota = float(input(f'Nota {i + 1}: '))
            if 0 <= nota <= 10:
                break
            print('<ERRO> Opção inválida! Digite uma nota entre 1 e 10.')
        notas.append(nota)
        soma += nota

    registro.append(notas[:]) # Adiciona a lista de notas ([n1, n2])


    media = soma / 2
    registro.append(media)

    #Adiciona o registro completo à ficha principal
    ficha.append(registro[:])

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('<ERRO> Opção inválida! Digite S ou N.')
    if opcao == 'N':
        break
print(ficha)
print('-=' * 25)
print('{:<4}{:<15}{:>8}'.format('Nº', 'NOME', 'MÉDIA'))
print('-' * 27)

for i, aluno in enumerate(ficha):
    nome = aluno[0]
    media = aluno[2]
    print(f'{i:<4}{nome:<15}{media:>8.1f}')
print('-' * 27)

#Exibir notas individuais do aluno
while True:
    aluno_id = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno_id == 999:
        break
    if 0 <= aluno_id < len(ficha):
        nome_aluno = ficha[aluno_id][0]
        notas_aluno = ficha[aluno_id][1]
        print(f'Notas de {nome_aluno} são: {notas_aluno}')
    else:
        print('<ERRO> Número de aluno inválido.')



