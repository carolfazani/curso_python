n= int(input('Digite um número: '))
print('O antecessor de {} é {} e seu sucessor é {}.'.format(n, n-1, n+1))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.4f}.'.format(n, d, t, r))

#ou

print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.4f}.'.format(n, (n*2), (n*3), (pow(n, (1/2)))))
