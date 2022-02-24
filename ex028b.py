from random import randint
import pygame
pygame.mixer.init()

computador = randint(1, 9)

print('SEJA BEM VINDO AO JOGO! SEU DESAFIO É DESCOBRIR QUAL NÚMERO O COMPUTADOR ESCOLHEU. VAMOS LÁ?')

usuário = 0
contagem = 0

while usuário != computador and usuário != 'SAIR':
    usuário = input('Digite um número de 1 à 9:  ').upper()

    if usuário == 'SAIR':
        print('Arregou')
        break

    contagem = contagem + 1

    if int(usuário) == computador:
        print('AE CARAI CE GANHOU DO COMPUTADOR PORRA! Número de tentativas: {}.'.format(contagem))
        pygame.mixer.music.load('win.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
        break

    elif int(usuário) < computador:
        print('Hmm, um pouco mais, tenta de novo!')
        pygame.mixer.music.load('loser.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass
    else:
        print("Hmm, um pouco menos, tenta de novo!")
        pygame.mixer.music.load('loser.mp3')
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()): pass


