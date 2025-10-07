'''
Exercício 094 - Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
lista. No final, mostre:
a - Quantas pessoas foram cadastradas.
b - A média de idade do grupo.
c - Uma lista com todas as mulheres.
d - Uma lista com todas as pessoas com idade acima da média.
'''

ficha = dict()
pessoas = list()
mulheres = list()
soma_idade = media_idade = nr_pessoas = 0
while True:
    nome = str(input('Nome: ')).strip()
    ficha['nome'] = nome


    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            ficha['sexo'] = sexo
            if sexo == 'F':
                mulheres.append(nome)
            break
        else:
            print('<ERRO> Opção inválida!! Digite M ou F.')

    while True:
        idade = int(input('Idade: '))
        if idade > 0:
            soma_idade += idade
            ficha['idade'] = idade
            break
        else:
            print('<ERRO> Opção inválida!! Digite uma idade maior que 0.')

    pessoas.append(ficha.copy())

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print('<ERRO> Opção inválida!! Digite S ou N.')
    if opcao == 'N':
        break
nr_pessoas = len(pessoas)
media_idade = soma_idade / nr_pessoas
print(pessoas)
print(mulheres)
print('-='*30)
print(f'- O grupo tem {nr_pessoas}.')
print(f'- A média de idade é de {media_idade:.2f} anos.')
print(f'- A(s) mulher(es) cadastrada(s) foram: {mulheres}')
print(f'- Lista das pessoas cadastradas que estão com idade acima da média: ')
for p in pessoas:
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
