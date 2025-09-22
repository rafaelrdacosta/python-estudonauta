'''
Aula 013 - Estrutura de repetição FOR
'''

#a contagem do laço não considera o último número
for c in range(1, 6):
    print('Oi')
print('FIM')

for c in range(0, 6):
    print(c, end=' ')
print('FIM')

for c in range(6, 0, -1): #-1 é para contagem regressiva
    print(c, end=' ')
print('FIM')

for c in range(0, 7, 2): #2 será o salto
    print(c, end=' ')
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c, end=' ')
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c, end=' ')
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

soma = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    soma += n
print(soma)



























