'''
Exercício 105 - Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''

def notas(*notas, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos(aceita quantos forem necessárias)
    :param sit: True, False ou não insere o valor, opcional, indicando se retornará ou não a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    ficha_aluno = dict()
    ficha_aluno['total'] = len(notas)
    maior = menor = media = soma = 0
    contador = 0
    for nota in notas:
        if contador == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        ficha_aluno['maior'] = maior
        ficha_aluno['menor'] = menor
        contador += 1
        soma += nota

    media = soma / len(notas)
    ficha_aluno['média'] = media

    if sit == True:
        if media < 5:
            situacao = 'RUIM'
        elif media < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        ficha_aluno['situação'] = situacao

    return ficha_aluno


#Programa principal
help(notas)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
resp2 = notas(9, 7, 2, 1, sit=False)
resp3 = notas(7, 5, 3)
print(resp)
print(resp2)
print(resp3)