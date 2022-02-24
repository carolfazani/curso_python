for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1: #o primeiro peso sempre será o maior e o menor ao mesmo tempo!
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso digitado foi {maior :.2f}Kg e o menor foi {menor :.2f}Kg.')
