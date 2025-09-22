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

string = str(input('Digite um string: ')).strip().split()

string1 = ''.join(string)
string2 = ''
for c in range(len(string1) - 1, -1, -1):
   string2[c] = string1[c]

if string2 == string1:
    print('A string é um políndromo.')
else:
    print('A string não é um políndromo.')



