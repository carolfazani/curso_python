def maior(*d):
    d = list()
    r = 's'
    while r in "sS":
        n = int(input('Digite um número'))
        d.append(n)
        e = sorted(d[:])
        r = input('Deseja continuar? [S/N]:')
    else:
        print('O maior valor digitado foi: ')
    print(e[-1])
maior()