def leiaInt(string):
    while True:
        try:
            num = str(input(f'{string} ')).strip()
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            try:
                num_int = int(num)
            except (ValueError, TypeError):
                print('\033[0;31m<ERRO> Por favor, digite um número inteiro válido!\033[m')
            else:
                return num_int

def linha(tam = 42):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(f'{msg:^40}')
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua opção: \033[m')
    return opc