from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f' Os números sorteados foram {sorteio}, sendo o maior {max(sorteio)} e o menor {min(sorteio)}')
