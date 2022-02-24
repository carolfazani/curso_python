print('-=-'*15,'\n          LOJÃO DA ZONA LESTE\n','-=-'*15)
nomeproduto = ' '
preço = ' '
total = 0
maismil = 0
c = 0
while True:
    nomeproduto = str(input('Nome do produto: '))
    preço = float(input('Preço:'))
    c += +1
    total+= +preço
    if preço > 1000.:
        maismil += +1
    if c == 1:
        maisbarato = preço
    if preço < maisbarato:
        maisbarato = preço
        nome = nomeproduto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'O total gasto na compra foi {total}. \n {maismil} produtos custaram mais de R$1000,00. \n O produto mais barato foi {nome}. ')





