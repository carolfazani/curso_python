from random import randint
from time import sleep
qjogos = int(input('Quantos jogos você irá fazer? '))

for c in range(0, qjogos):
    aposta = []
    while len(aposta) <6:
        número = randint(1, 60)
        if número not in aposta:
            aposta.append(número)
    sleep(1)
    print(f'Jogo {c + 1}: {aposta}')