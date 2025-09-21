'''
Exercício 042 - refaça o desafio 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo
será formado.
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes.
'''

s1 = float(input('Informe o valor do 1º segmento de reta: '))
s2 = float(input('Informe o valor do 2º segmento de reta: '))
s3 = float(input('Informe o valor do 3º segmento de reta: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os três segmentos de reta formam um triângulo.')
    if s1 == s2 and s2 == s3:
        print('Triângulo Equilátero!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Triângulo Isósceles!')
    else:
        print('Triângulo Escaleno!')
else:
    print('Os três segmentos de reta não formam um triângulo.')