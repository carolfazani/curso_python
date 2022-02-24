tupla = (int(input('Primeiro número: ')), int(input('Segundo número: ')),
         int(input('Terceiro número: ')), int(input('Quarto número: ')))
print(f'Você digitou os valores{tupla}. '
      f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'o valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print('O valor 3 não aparece em nehuma posição.')
print('Os valores pares são:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')