'''
Exercício 083 - Crie um programa onde o usuário digite uma expressão qualquer que
parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.
'''

abertos = fechados = 0
expressao = str(input('Digite uma expressão: ')).strip()
for i in range(0, len(expressao)):
    if expressao[i] == '(':
        abertos += 1
    if expressao[i] == ')':
        fechados += 1

if abertos == fechados:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')


