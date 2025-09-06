'''
Aula 007 - Operadores Aritméticos
'''
print(5 + 2, '- Soma')
print(5 - 2, '- Subtração')
print(5 * 2, '- Multiplicaçaõ')
print(5 / 2, '- Divisão')
print(5 ** 2, '- Potência')
print(5 // 2, '- Divisão inteira')
print(5 % 2, '- Módulo ou Resto da Divisão')

print(5 + 3 * 2) #precedência => primeiro *
print(3 * 5 + 4 ** 2) #precedência => primeiro **, depois *
print(3 * (5 + 4) ** 2) #precedência => parêntese, potência, multiplicação

print(81**(1/2)) #raiz quadrada
print(127**(1/3)) #rais cúbica

print('=' * 20, '\n')

nome = 'Rafael'
print('Prazer em te conhecer {:20}!'.format(nome)) #o nome irá ocupar 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhamento a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinhamento a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) #centralizado com caractere

n1 = 4
n2 = 8
s =  n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\nA soma vale {}'.format(n1 + n2))
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira é {} e a potência é {}'.format(di, e), end=' ')
print('Colocar end e uma string vazia no print anterior evita quebrar a linha')