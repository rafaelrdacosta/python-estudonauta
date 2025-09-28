'''
Exercício 075 - Desenvolva um programa que leia
quatro valores pelo teclado e guarde-os em uma
tupla. No final mostre:
a - Quantas vezes apareceu o valor 9.
b - Em que posição foi digitado o primeiro valor 3.
c - Quais foram os números pares.
'''

numeros = ()
for c in range(0, 4):
    n = int(input(f'Digite o {c+1}º número: '))
    numeros += (n, )

print('Você digitou os valores {}'.format(numeros))

qtd_nove = numeros.count(9)
if qtd_nove > 0:
    print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')
else:
    print('O número 9 não foi digitado.')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')

contador = 0
pares = ()
for numero in numeros:
    if numero % 2 == 0:
        contador += 1
        pares += (numero, )
print(f'Os valores pares digitados foram {pares}')