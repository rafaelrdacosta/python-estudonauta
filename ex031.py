'''
Exercício 031 - Desenvolva um programa que pergunte
a distância de uma viagem em km. Calcule o preço da
passagem, cobrando  R$0.5 por km para viagens até 200km
e R$0.45 para viagens mais longas.
'''

dist = float(input('Qual a distância de sua viagem em Km? '))

if dist > 200:
    print('Valor da passagem: R${:.2f}'.format(dist*0.45))
else:
    print('Valor da passagem: R${:.2f}'.format(dist*0.5))