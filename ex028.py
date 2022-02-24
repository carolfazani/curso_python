from random import choice
import pygame
pygame.mixer.init()
def open_txt_tab(path):
    with open(path, "r", encoding="utf-8") as file:
        return [int(file.read())]
    file.close()
n = open_txt_tab('C:\\regradojogo.txt')
n = n[0]
computador = (choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


print('SEJA BEM VINDO AO JOGO! SEU DESAFIO É DESCOBRIR QUAL NÚMERO O COMPUTADOR ESCOLHEU. VAMOS LÁ?')
usuário = int(input('Digite um número de 0 à 9:  '))
print('O número escolhido pelo computador foi {}.'.format(computador))


if usuário == computador:
    print('Parabéns, você acertou!')
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass

else:
    result = 'Você errou '
    pygame.mixer.music.load('loser.mp3')
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy()):pass
    if usuário - n == computador:
        result += "para mais!"
    elif usuário + n == computador:
        result += 'para menos!'
    else:
        result += 'feio!'
    print(result)


