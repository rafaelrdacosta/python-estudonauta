'''
Aula 16 - Estruturas compostas
Tuplas'''


lanche = 'sanduiche', 'suco', 'pizza', 'pudim'
print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:]) #do elm 1 até o fim
print(lanche[:2]) #do início até o elemento 1 (exclui o 2)
print(lanche[-1])  #pudim

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!\n')

for cont in range (0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

print(c.count(5))
print(c.index(5))
print(c.index(5,2))

pessoa = ('Rafael', 44, 'M', 91.2)
print(pessoa)

del(pessoa)
print(pessoa)

#lanche[0] = 'hamburguer' #irá ocorrer um erro, tuplas são IMUTÁVEIS