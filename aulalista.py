lista = ['arroz', 'feijão', 'batata', 'macarrão', 'chuchu', 'banana', 'abóbora']
lista[0] = 'arroz integral' #subistitui itens
lista.append('ovo') #adc no final
lista.insert(3, 'chocolate') #adc na posição 3
del lista[8] #remove o item 8
lista.pop(0) #remov o item 0
lista.remove('chuchu') #remove chuchu
valores = list(range(4, 10)) # de 4 até 9.
valores2= list(range(4, 10, 2)) # de 4 até 9 pulando de 2 em 2
numeros = [6, 4, 3, 4, 8, 9]
numeros.sort() #coloca em ordem
numeros.sort(reverse=True) #coloca em ordem reversa
len(valores) #tamanho da lista
numeros.insert(0, 2) #na posição 0 insere 2
numeros.pop()#elimina o ultimo valor
numeros.pop(0)#elimina primeiro valor
numeros.remove(4)#elimina o primeiro 4 que aparecer
listas = [[], []] #duas listas dentro de uma lista.

#modo 1
val = list()
val.append(0)
val.append(1)
val.append(7)

for c, v in enumerate(val):
    print(f'Na posição {c} está o valor {v}!')

#modo 2
val2 = list()

for cont in range(0, 5):
    val2.append(int(input('Digite um valor: ')))

for c, v in enumerate(val2):
    print(f'Na posição {c} está o valor {v}!')

#relacionar listas
a = [1, 3, 5, 8]
b = [1, 3, 5, 8]
b = a
b[2] = 5 #nesse momentos a posição 2 das duas listas são substituidas

#copiar listas
a = [1, 3, 5, 8]
b = a[:] #b recebe valores de a sem criar ligação

