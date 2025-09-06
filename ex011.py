'''
Exercício 011 - Faça um programa que leia a largura
e a altura de uma parede em metros, calcule a sua
área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m²
'''

largura = float(input('\nQual a largura da parede (m)? '))
altura = float(input('Qual a altura da parede (m)? '))
area = largura * altura
print('A área da parede de {}mx{}m é igual a {:.2f}m².'.format(largura, altura,area))
print('Será necessário {:.2f} litros de tinta.'.format(area/2))
