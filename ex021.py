'''
Exercício 021 - Faça um programa que abra e reproduza o áudio
de um arquivo MP3.
'''
import time
import pygame

# 1. Inicializa o mixer do Pygame
pygame.mixer.init()

# 2. Carrega e reproduz o arquivo MP3
pygame.mixer.music.load('amor_fe.mp3')


# 3. Exibe as intruçoes e inicia a música
print('Controles:\nPause\nPlay\nTerminar')
pygame.mixer.music.play()

#4. Loop controle de reprodução
while True:
    comando = input('>> ')
    if comando.lower() == 'pause':
        pygame.mixer.music.pause()
        print('Música pausada.')
    if comando.lower() == 'play':
        pygame.mixer.music.unpause()
        print('Tocando música.')
    if comando.lower() == 'terminar':
        pygame.mixer.music.stop()
        print('Música encerrada.')
        break
    #Adiciona um pequeno atraso para não sobrecarregar o processador
    time.sleep(0.1)


# 5. Encerra o Pygame quando a música acabar (opcional)
pygame.mixer.quit()

