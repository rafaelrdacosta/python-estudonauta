'''
Aula 010 - Condições
'''

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')


#Condição simplificada
print('Carro Novo!'if tempo<=3 else 'Carro Velho!')

print('--FIM--')