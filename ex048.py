soma = 0
for c in range(0, 500):
    if c%2 ==1 and c%3 ==0:
        soma += c
print(f'O valor da soma de todos números multiplos de 3 entre 0 e 500 é {soma}')