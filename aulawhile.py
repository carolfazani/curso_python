# for c in range(1, 10):
   # print (c) #se não sabe o limite n usa o for


c=1
while c < 10:
    c+=1
    print(c)

n=1
while n!=0:
    n = (int(input('Digite um número')))
print('End') #sai do laço

r = 'S'
while r == 'S':
    n= int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('End')

n = s = 0
while True:
    n = (int(input('Digite um número')))
    if n == 10:
        break
    s += n
salário = 905.3
print(f'O soma é {s} e o salário é R${salário:.2f}') #f string