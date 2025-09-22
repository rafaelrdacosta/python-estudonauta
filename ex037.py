'''
Exercício 037 - Escreva um programa que leia um
número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
opcao =  int(input('''Escolha a base para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Digite a opção: '''))

if opcao == 1:
    print('{} em Binário é igual a: {}'.format(num, bin(num)[2:])) #[2:] para retirar o prefixo
elif opcao == 2:
    print('{} em Octal é igual a: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em Octal é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')