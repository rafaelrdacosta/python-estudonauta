'''
Exercício 63 - Escreva um programa que leia um
número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Digite a quantidades de elementos para exibir a Sequência de Fibonacci: '))

'''lista = [0, 1]
c = 1
while c < n - 1:
    fibo = lista[c] + lista[c-1]
    lista.append(fibo)
    c += 1
    print(lista[c], end=' -> ')
print('FIM')'''
t1 = 0
t2 = 1
print('{} - > {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
