princ= [[], []]

for p in range(0, 7):
    núm = int(input('Digite um número: '))
    if núm % 2 == 0:
        princ[0].append(núm)
    else:
        princ[1].append(núm)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram {princ[0]} e os impares foram {princ[1]}')