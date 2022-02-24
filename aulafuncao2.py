
def contador (i, f, p):
    #docstrings
    '''
    faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: pulo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')

contador( 2, 9, 2)

help(contador) #para acessar a docstring


def soma (a= 0, b=0, c=0): #=0 é para colocar um parâmetro como opcional.
    s = a + b + c
    return s

r1= soma(b=2, c=4)
r2 = soma( 2, 4, 6)
r3 = soma (3, 6, 8)

print(f'Os resultados foram {r1}, {r2} e `{r3}.')

#escopo de varáveis: variaveis declaradas dentro da função só existem dentro da função,
# ... são variaveis locais, e delcaradas fora são variaveis globais.

def teste(b):
    # global a > se tira o comentário a fica com o valor de fora apenas.
    a= 8
    b = 5
    c= 5
    print(f'A  dentro vale {a}')
    print(f'B  dentro vale {b}')
    print(f'C  dentro vale {c}')

a= 5
teste(a)
print(f'A fora vale{a}')

'''