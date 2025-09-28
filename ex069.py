'''
Exercício 069 - Crie um programa que leia a idade e o
sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
a - Quantas pessoas tem mais de 18 anos.
b - Quantos homems foram cadastrados.
c - Quantas mulheres tem menos de 20 anos.
'''

maior_idade = total_homem = menos_vinte = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 30)

    if idade >= 18:
        maior_idade += 1

    if sexo == 'M':
        total_homem += 1
    elif sexo == 'F' and idade < 20:
        menos_vinte += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    # Sai do programa se a opção for 'N'
    if opcao == 'N':
        break

print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo tem(os) {total_homem} homen(s) cadastrado(s).')
print(f'E temos {menos_vinte} mulher(es) com menos de 20 anos.')

