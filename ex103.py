def ficha(n=0, g=0):

    print(f'O jogador {n}, fez {g} gols.')


n = str(input('nome'))
g = str(input('gol'))
if n == '':
    n = '<desconhecido>'
if g == '' or not g.isnumeric():
    g = '<null>'

ficha(n=n, g=g)
