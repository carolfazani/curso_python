números = list()
maiorvalor = []
menorvalor = []
for c in range(0, 5):
    números.append(int(input('Digite um número: ')))

print(f'Você digitou os valores {números}')

print(f'O maior valor digitado foi {max(números)}  na posição {números.index(max(números))}')

print(f'O menor valor digitado foi {min(números)} na posição {números.index(min(números))}')
