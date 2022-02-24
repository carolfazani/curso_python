número = int(input('Digite um valor: '))
contagem = número
fatorial = 1
print(f'Calculando {número}!...')
while contagem > 0:
    print(f'{contagem}', end='')
    print(' x ' if contagem > 1 else ' = ', end='')
    fatorial = fatorial * contagem
    contagem = contagem - 1
print(fatorial)