
for c in range(0, 6): #conta de 1 até 5 e c pode ser qqr coisa
    print(c)
print('-'*10)
for c in range(6, 0, -1): #conta de 6 até 0
    print(c)
print('-'*10)
for c in range(0, 6, 2): #conta pulando de 2 em 2
    print(c)
print('-'*10)
n= int(input("digite um número:"))
for c in range(0, n+1):
    print(c)
print('-'*10)
i= int(input("Inicio")) #pular de quanto em quanto?
f= int(input('Final'))
p= int(input('Pulo'))
for x in range(i, f+1, p):
    print(x)
print('-'*10)
linha = 0
for x in range(0, 5):#soma os valores dentro do laço
    n = int(input('Digite um número: '))
    linha += 1
print('soma {}'.format(linha))
