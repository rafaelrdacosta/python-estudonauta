'''
Exercício 085 - Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]
num = 0
for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('-='*25)
print(f'Todos os valores: {numeros}')
print(f'O valores pares digitados foram: {sorted(numeros[0])}')
print(f'Oa valores ímpares digitados foram: {sorted(numeros[1])}')