
def leiaDinheiro(msg):
    """
    Função que força o usuário a digitar um valor que pode ser convertido
    para um número (float). Repete a solicitação até que a entrada seja válida.
    """
    valido = False

    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()

        # 1. TRATAMENTO: Tenta converter a string para float
        try:
            valor_numerico = float(entrada)
            valido = True # Se a conversão for bem-sucedida, a flag é True

        except ValueError:
            # Se a conversão falhar (ex: 'texto', '10a')
            print(f'\033[31mERRO! "{entrada}" é um preço inválido.\033[m')

    return valor_numerico