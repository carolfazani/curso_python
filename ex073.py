campeonato = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(f' Os cinco primeiros colocados são{campeonato[:5]}')
print(f' Os 4 últimos colocados são {campeonato[-4:]}')
print(f' Lista dos times em ordem alfabética: {sorted(campeonato)}')
print(f' O Chapecoense está na {campeonato.index("Chapecoense")} posição.')