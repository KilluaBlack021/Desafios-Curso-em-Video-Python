# tocando uma musica com python

import pygame
from time import sleep

# inicia o mixer e carrega a musica
pygame.mixer.init()
pygame.mixer.music.load('Cross Road Blues (Take 1).mp3')

# perfumaria, não é importante, ta aqui só pra aparecer bonitinho na execução
print('')
print('\nOlá!', end='')
sleep(1)
print('Tocarei ', end='')
sleep(.5)
print('uma musica ', end='')
sleep(.5)
print('pra tu!')
sleep(2)
print('Toma', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.')
sleep(1)

# tocando a musica, enfim
pygame.mixer.music.play()
print('Tocando Cross Road Blues (Take 1) - Robert johnson')
sleep(1)
print('Eae! Curtiu?')
while pygame.mixer.music.get_busy():
    continue
