'''
Exercício 049 - Refaça o exercício 009, mostrando
a tabuada de um número que o usuário escolher, só
que agora utilizando o laço for.
'''

n = int(input('Digite o número para exibir sua tabuada: '))
print('=-'*7)
print('Tabuada de {}'.format(n))
for c in range(1, 11):
    print('{} x {:>2} = {:>2}'.format(n, c, n * c))
print('=-'*7)