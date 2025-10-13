'''
Exercício 112 - Dentro do pacote de utilidadesCev que criamos no exercício 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
capaz de funcionar como a função input, mas com uma validade de dados para
aceitar valores que sejam monetários.
'''

from ex112.utilidadesCev import dado, moeda


p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)