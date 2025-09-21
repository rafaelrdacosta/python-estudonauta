'''
Exercício 043 - Desenvolva uma lógica que leia o peso
e a altura de uma pessoa, calcule seu IMC e mostre seu
status, de acordo com a tabela abaixo:
Menor que 18,5: Abaixo do peso
Entre 18,5 e 24,9: Peso ideal
Entre 25 e 29,9: Sobrepeso
Entre 30 e 34,9: Obesidade grau I
Entre 35 e 39,9: Obesidade grau II
Maior que 40: Obesidade grau III
'''


peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
IMC = peso / (altura ** 2)

print('IMC: {:.1f} - '.format(IMC), end='')

if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif IMC < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif IMC < 30:
    print('Você está com SOBREPESO.')
elif IMC < 35:
    print('Você está em Obesidade grau I.')
elif IMC < 40:
    print('Você está em Obesidade grau II.')
else:
    print('Você está em Obsedidade grau III (mórbida).')