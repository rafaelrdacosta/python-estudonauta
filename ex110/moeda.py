'''
Exercício 110 - Adcione ao módulo moeda.py criado nos exercícios anteriores, uma
função chamada resumo(), que mostre na tela alguamas informações geradas pelas
funções que já temos no módulo criado até aqui.
'''

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace('.', ',')

def aumentar(preco=0, porcentagem=0, formatar=False):
    resultado = preco + (porcentagem / 100 * preco)
    if formatar:
        return moeda(resultado)
    else:
        return resultado

def diminuir(preco=0, porcentagem=0, formatar=False):
    resultado = preco - (porcentagem / 100 * preco)
    if formatar:
        return moeda(resultado)
    else:
        return resultado

def dobro(preco=0, formatar=False):
    resultado = preco * 2
    if formatar:
        return moeda(resultado)
    else:
        return resultado

def metade(preco=0, formatar=False):
    resultado = preco / 2
    if formatar:
       return moeda(resultado)
    else:
        return resultado

def resumo(preco=0, aumento=10, desconto=5):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'Preço analisado: {moeda(preco):>18}')
    print(f'Dobro do preço: {dobro(preco, True):>19}')
    print(f'Metade do preço: {metade(preco, True):>18}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento, True):>19}')
    print(f'{desconto}% de redução: {diminuir(preco, desconto, True):>19}')
    print('-' * 35)

