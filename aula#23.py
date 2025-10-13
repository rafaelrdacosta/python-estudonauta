'''
Aula 23 - Tratamento de erros e exceções
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'Problema encotrado foi {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte Sempre! Muito obrigado!')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dado que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte Sempre! Muito obrigado!')