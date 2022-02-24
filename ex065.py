ques = 'S'
c = soma = maior = menor = 0
while ques == 'S':
    c += 1
    núm = int(input('Digite um número: '))
    ques = str(input('Deseja continuar? [S/N]')).strip().upper()
    soma +=núm
    média = soma/c
    if c == 1:
        maior = menor = núm
    if núm > maior:
        maior = núm
    if núm < menor:
        menor = núm
else:
    print(f'Você digitou {c} números e sua média foi {média:.2f}')
    print(f'O maior número foi {maior} e o menor foi {menor}. ')