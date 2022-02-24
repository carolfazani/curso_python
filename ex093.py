dados = dict()
dados['nome'] = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
dados['gols'] = list()
for v in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {v}?'))
    dados['gols'].append(gol)
dados['total'] = sum(dados['gols'])
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(dados['gols']):
    print(f'Na partida {k} fez {v} gols')
print(f'foi um total de {dados["total"]} gols')
