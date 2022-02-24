from random import randint
numeros = list()

def sorteia():
    for x in range(0, 10):
        a =randint(0, 10)
        numeros.append(a)
    print(numeros)

def somaPar():
    par = list()
    for y in numeros:
        if y %2==0:
            par.append(y)
    print(sum(par))

sorteia()
somaPar()