'''
Exercício 080 - Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar
o sort()).
No final, mostre a lista ordenada na tela.
'''

lista = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))

    # Se for o primeiro elemento OU se for maior que o último da lista
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            # Se o novo número (n) for menor ou igual ao elemento atual da lista (lista[pos])
            if n <= lista[pos]:
                # Insere o novo número nessa posição
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break  # É CRUCIAL SAIR DO LOOP assim que a inserção é feita
            pos += 1
print('-='*25)
print(f'Os valores digitados em ordem foram {lista}')
