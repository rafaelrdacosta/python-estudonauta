'''
Aula 09 - Manipulando Texto
'''

frase = '  Curso em Vídeo Python  '

print(frase[3])
print(frase[3:13])
print(frase[:14])
print(frase[15:])
print(frase[1:15])
print(frase[1:15:2]) #início, fim, salto
print(frase[1::2])
print(frase[::2])

print('''\nANSI - escape sequence
Representação de cores - 033C[<código da cor>m
código da cor = style;text;back''')

print(frase.count('o')) #case sensitive
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #não muda definitivamente, somente se atribiuir a outra variável
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][1])
print('-'.join(dividido))