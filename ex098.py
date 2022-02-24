#não terminei, olha a resposta na aula. 
def contador(inicio, fim, passo):
    if inicio < fim:
        c = inicio
        while c <=fim:
            c += passo
            print(f'{c}', end='-')
        print('Fim')
    else:
        c = inicio
        while c >=fim:
            c -= passo
            print(f'{c}', end='-')
        print('Fim')

print('Contagem até 10 de 1 em 1')
contador(0, 10, 1)
print('Contagem até 10 de 2 em 2')
contador(10, 0, 2)
print('Personalize a sua contagem!')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(inicio=i, fim=f, passo=p)

