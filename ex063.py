termos = int(input('Quantos termos você quer mostrar? '))
antecessor = 0
sucessor = 1
fibonacci = antecessor + sucessor
print(f'{antecessor} → {sucessor}', end=' → ')
c = 3
while c <= termos:
    fibonacci = antecessor + sucessor
    antecessor = sucessor
    sucessor = fibonacci
    c+= +1
    print(f'{fibonacci}  → ', end='')
print('FIM')
