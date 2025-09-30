'''
Aula 017 - Listas
'''
'''
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
#num[4] = 7 #fora do range
num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(f'Esta lista tem {len(num)} elementos.')

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

num.insert(2, 3)
print(num)

num.remove(3) #vai eliminar a primeira ocorrência do valor passado
print(num)

if 4 in num:
    num,remove(4)
else:
    print('Não achei o número 4.')

lista = []
lista.append(5)
lista.append(9)
lista.append(4)
for item in lista:
    print(f'{item}...', end='')

for indice, item in enumerate(lista):
    if indice == 0:
        print('\n')
    print(f'Na posição {indice} econtrei o valor {item}!')

for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)'''

a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 #vai atribuir as duas listas
print(f'\nLista A: {a}')
print(f'Lista B: {b}')

b = a[:] #copia todos valores de a e atribui a b
b[2] = 9
print(f'\nLista A: {a}')
print(f'Lista B: {b}')
