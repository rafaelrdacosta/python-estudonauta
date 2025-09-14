'''
Exercício 026 - Faça um programa que leia uma frase
pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase:')).strip().upper()

#print(frase)
print('A frase tem {} letras.'.format(len(frase)))
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na {}º posição.'.format(frase.find('A')+1))
print('A última letra A apareceu na {}º posição.'.format(frase.rfind('A')+1))