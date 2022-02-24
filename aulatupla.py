
f = ('arroz', 'feijão', 'batata', 'macarrão', 'chuchu', 'banana', 'abóbora')
print(f)
print(f[3:5])
print(f[0:7:2]) #mostra 2 em 2
print(f[:5]) #mostra até o 5
print(f[5:]) #mostra do 5 pra frente
print(f[2::6]) #conta caracteres
print(f[-2])
print(f[-2:]) #começa no -2 de vai até o final
print(len(f)) #conta os itens
print(sorted(f)) #ordem alfabetica

for posição, comida in enumerate(f):
    print(f'Eu vou comer {comida} na posição {posição}')

for c in range (0, len(f)):
    print(f'Eu vou comer {f[c]} na posição {c}')

a= (1, 5, 'arroz', 4)
b = (5, 6, 5, 8)
c = a + b
print(c)
print(len(c))
print(c.count(5)) #qtas vezes o 5 aparece
print(c.index(5)) # primeira posição q o 5 aparece
print(c.index(5, 4)) # primeira posição q o 5 aparece dps da posição 4
#del(f) #apaga a tupla toda
