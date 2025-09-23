'''
Exercício 053 - Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.
Exemplos:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''

string = str(input('Digite um string: ')).strip().upper()

#Split cria uma lista de palavras e com join irá juntar sem espaços
string_sem_espacos = ''.join(string.split())

string_invertida = string_sem_espacos[::-1]
'''string_invertida = ''
for letra in range(len(string_sem_espacos) - 1, -1, -1):
    string_invertida += string_sem_espacos[letra]'''

print('O inverso de {} é {}'.format(string_sem_espacos, string_invertida))
if string_sem_espacos == string_invertida:
    print('A string é um palíndromo.')
else:
    print('A string não é um palíndromo.')


