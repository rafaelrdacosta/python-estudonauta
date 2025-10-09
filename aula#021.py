'''
Aula 021 - Funções 2ª parte
'''

help(len)

print(input.__doc__)

def contador(i, f, p):
    #Docstrings entre aspas triplas abaixo
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

#Parâmetros opcionais
def somar(a, b, c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor, que é opcional (c = 0)
    :return:
    '''
    s = a + b + c
    print(f'A soma vale {s}')

def teste():
    x = 8 #Escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

def funcao():
    n1 = 4
    print(f'N1 dentro da função vale {n1}')

def multiplicar(a=0, b=0, c=0):
    m = a * b * c
    return m

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f



#Programa principal
help(contador)
contador(2, 10, 2)
somar(3, 2, 5)
somar(8, 3)

#Escopo global
n = 2
print(f'No programa principal, n vale {n}')
teste()

n1 = 2
print(f'N1 global vale {n1}')
funcao()

print(multiplicar(2, 3, 4))
resposta = multiplicar(6, 2, 1)
print(resposta)

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


