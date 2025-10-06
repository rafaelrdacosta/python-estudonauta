'''
Aula 19 - Dicionários
'''

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #as chaves tem que ser entre aspas duplas
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k}: {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)

pessoas['peso'] = 98.5
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brazil.append(estado.copy())
print(brazil)

for e in brazil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')




