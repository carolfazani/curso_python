#lista dentro de listas

pessoas = [['Carol', 29], ['Caio', 5], ['Rodrigo', 30], ['Gustavo', 25]]
print(pessoas[0][1]) #elemento 1 da lista 0

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')

#exemplo 01
lista = list()
lista.append('Carol')
lista.append('29')
lista2 = list()
lista2.append(lista[:])
lista[0]= ('Caio')
lista[1]= ('5')
lista2.append(lista[:])
print(lista2)


#exemplo 02
galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Digite o seu nome: ')))
    dados.append((int(input('Digite a sua idade: '))))
    galera.append(dados[:]) #{[:] copia dados pra galera
    dados.clear() #exclui lista dados
print(galera)
