n = 1

while n > 0:
    n = int(input('Digite um número: '))
    c = 0
    if n < 0:
        print('Programa Finalizado. ')
        break
    while c <= 10:
        resultado = n*c
        print('{} x {} = {}'.format(n, c, resultado))
        print('-'*20)
        c+= + 1






