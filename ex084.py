pessoa = []
lista = []
maior = menor = 0

while True:
   pessoa.append(str(input('Nome:')))
   pessoa.append(float(input('Peso:')))
   if len(lista) == 0:
       maior = menor = pessoa[1]
   else:
       if pessoa[1] > maior:
           maior =pessoa[1]
       if pessoa[1] < menor:
           menor = pessoa[1]
   lista.append(pessoa[:])
   pessoa.clear()
   continua = str(input('Deseja continuar? [S/N]')).upper().strip()
   if continua == 'N':
        break


print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {maior}, da(s) pessoa(s): ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end= '')
print()
print(f'O menor peso foi {menor}, da(s) pessoa(s): ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]')