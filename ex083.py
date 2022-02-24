expre = input('Digite uma expressão: ')
aberto = []
for v in expre:
    if v == '(':
        aberto.append(v)
    elif v == ')':
        if len(expre) > 0:
            aberto.pop()
        else:
            aberto.append(')')
            break

if len(aberto) == 0:
    print('valido')
else:
    print('invalido')



print(aberto,expre)