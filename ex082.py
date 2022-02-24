números = []
pares = []
impares = []
while True:
    números.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continua == 'N':
        for v in números:
            if v % 2 == 0:
                pares.append(v)
            else:
                impares.append(v)
        print(f'Valores da Lista: {números}. Valores pares {pares} e impares {impares}')
        break
