'''
Aula 11 - Cores no terminal
'''

#Cor no terminal - \033[style;text;backm
print('\033[31mOlá, Mundo!!')
print('\033[1;31;43mOlá, Mundo!!\033[m') #\033[m => tira as configurações
print('\033[4;31;46mOlá, Mundo!!\033[m')
print('\033[1;30;45mOlá, Mundo!!\033[m')
print('\033[30mOlá, Mundo!!\033[m')
print('\033[7;30mOlá, Mundo!!\033[m')

a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m.'.format(a, b))

nome = 'Rafael'
print('Olá! Muito prazer em te conhecer {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'azul':'\033[34m',
         'amarelo':'\033[33m',
         'limpa':'\033[m'
}

print('Olá! Muito prazer em te conhecer {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))