'''
Exercício 062 - Melhore o exercício 061, perguntando para o
usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0
termos.
'''


t = int(input('\nDigite o 1º termo da Progressão Aritmética: '))
r = int(input('Digite a razão da PA: '))

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

print('Primeiro termo: {}'.format(t))
print('Razão: {}'.format(r))

total_termos = 10
termos_exibidos = 0

while termos_exibidos < total_termos:
    print(t, end=' ')
    t += r
    termos_exibidos += 1

    if termos_exibidos == total_termos:
        print('FIM')
        mais_termos = int(input('\nVocê deseja mostrar mais quantos termos? [0 para sair]: '))
        if mais_termos > 0:
            total_termos += mais_termos
        else:
            break
