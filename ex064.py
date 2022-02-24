número = c = soma = 0
número = int(input('Digite o número 999: '))
while número != 999:
    c += 1
    soma += número
    número = int(input('Digite o número 999:'))
else:
    print(f'O número de tentativas foi {c}, e a soma desses números é {soma}.')




