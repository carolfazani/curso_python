matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    for p in matriz[l]:
        if p % 2 == 0:
            soma = soma + p

print(f'A soma dos valores pares é {soma}.')
print(f'A soma da terceira coluna é {matriz[0][2] + matriz [1][2] + matriz [2][2]} ')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
