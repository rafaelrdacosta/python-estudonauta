'''
Exercício 109 - Modifique as funções que foram criadas no exercício 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai
ser ou não formatado pela função moeda(), desenvolvida no exercício 108.
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



