listavalor = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > listavalor[-1]:
        listavalor.append(valor) #quando vc adc o valor já vai pro final...
        print('Valor adicionado ao final da lista. ')
    else:
        pos = 0
        while pos < len(listavalor):
            if valor <= listavalor[pos]:
                listavalor.insert(pos, valor)
                print(f'O valor  foi adicionado na posição {pos}.')
                break
            pos+= 1

print('~~'*15)
print(f'Os valores digitados foram: {listavalor}')
print('~~'*15)






