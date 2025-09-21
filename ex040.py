'''
Exercício 040 - Crie um programa que leia duas notas de
um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''

n1 = float(input('\nDigite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2)/2

print('\nTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))

if media < 5.0:
    print('O aluno está REPROVADO!')
elif media < 7.0:
    print('O aluno está RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO!')
