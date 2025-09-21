'''
Exercício 044 - Elabore um programa que calcule o valor
a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- à vista dinheiro/cheque:  10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS GUANABRA '))
preco = float(input('Qual valor do produto? R$ '))
opcao = int(input('''Qual a forma de pagamento?
[ 1 ] - Á vista Dinheiro/Cheque
[ 2 ] - Á vista no Cartão
[ 3 ] - 2x no Cartão
[ 4 ] - 3x ou mais no Cartão
Digite a opção: '''))

if opcao == 1:
   total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    print('Sua compra será parcelada em 2x de R$ {:.2f}'. format(total/2))
elif opcao == 4:
    total = preco * 1.2
    parcelas = int(input(('Quantas parcelas? ')))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, total / parcelas))
else:
    total = preco
    print('Opção inválida!!')

print('Sua compra de R$ {:.2f} vai custar R$ {} no final.'.format(preco, total))

