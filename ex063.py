'''
Exercício 63 - Escreva um programa que leia um
número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

n = int(input('\nDigite a quantidades de elementos para exibir a Sequência de Fibonacci: '))

lista = [0, 1]
c = 1
while c < n - 1:
    fibo = lista[c] + lista[c-1]
    lista.append(fibo)
    c += 1
    print(lista[c], end=' -> ')
print('FIM')

