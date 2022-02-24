def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        valor = int(n)
        if n.isnumeric():
            ok = True
        else:
            print('Digite um número válido: ')
        if ok:
            break
        return valor


n = leiaInt('Digite um número: ')