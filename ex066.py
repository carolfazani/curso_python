c = soma = 0
while True:
    número = int(input('Digite o número 999: '))
    if número == 999:
        break
    c += 1
    soma += número
print(f'O número de tentativas foi {c}, e a soma desses números é {soma}.')