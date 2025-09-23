'''
Exercício 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final mostre:
- A média de idade do grupo.
- Qual o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
'''
soma_idade = 0
contador = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
for c in range(0, 4):
    print('=' * 20)
    print('Dados {}º pessoa'.format(c + 1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            contador += 1


media_idade = soma_idade / 4

print(f'\nA média das idades é igual a: {media_idade:.2f}.')

if nome_homem_mais_velho:
    print(f'O homem mais velho se chama {nome_homem_mais_velho} e tem {idade_homem_mais_velho} anos.')
else:
    print('Nenhum homem foi cadastrado.')

print(f'{contador} mulheres têm menos de 20 anos.')