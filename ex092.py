'''
Exercício 092 - Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano de contrataçaõ e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

funcionario = {}

funcionario['nome'] = str(input('Nome: ')).strip()

ano_atual = date.today().year
ano_nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nascimento
funcionario['idade'] = idade

while True:
    nr_CTPS = int(input('Carteira de Trabalho (0 não tem): '))
    if nr_CTPS == 0:
        break
    else:
        funcionario['ctps'] = nr_CTPS
        ano_contrato = int(input('Ano de contratação: '))
        funcionario['contratação'] = ano_contrato
        salario = float(input('Salário: R$ '))
        funcionario['salário'] = salario
        ano_aposentadoria = ano_contrato + 35
        idade_aposentadoria = (ano_aposentadoria - ano_atual) + idade
        funcionario['aposentadoria'] = idade_aposentadoria
        break
print('-='*30)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')