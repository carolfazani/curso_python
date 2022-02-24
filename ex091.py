from random import randint
from operator import itemgetter
dado = {
'jogador1':  randint(0, 6),
'jogador2':  randint(0, 6),
'jogador3':  randint(0, 6),
'jogador4':  randint(0, 6)
 }
ranking = dict()
for k, v in dado.items(): #chave e valor
    print(f' O {k} tirou {v}')
ranking = sorted(dado.items(), key=itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
