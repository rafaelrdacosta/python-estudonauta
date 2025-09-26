'''
Exercício 059 - Crie um programa que leia
dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Inserir novos números
[5] Sair do programa
Seu programa deverá realizar a operação
solicitada em cada caso.
'''

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

opcao = 0
while opcao != 5:
    opcao = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Inserir novos números
    [5] Sair do programa
    >>>>> Qual a opção desejada? '''))

    if opcao == 1:
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
        #break
    elif opcao == 2:
        print('A multiplação entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
        #break
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
        if n2 > n1:
            print('O número {} é maior que o número {}.'.format(n2, n1))
        else:
            print('Os números informados são iguais.')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando.')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 12)
print('Fim do programa! Volte Sempre!')


