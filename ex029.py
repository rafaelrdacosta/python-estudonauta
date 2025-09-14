'''
Exercício 029 - Escreva um programa que leia a
velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7.00 por km acima do limite.
'''

vel = float(input('Qual a velocidade do carro: '))

if vel > 80:
    print('Você ultrapassou o limite de 80km/h!')
    print('Valor da multa: R${:.2f}'.format((vel - 80)*7))

print('Siga em frente. Boa Viagem!')
