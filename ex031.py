distância= float(input('Quantos km de viagem será? '))
if distância <= 200:
    print('O preço da sua passagem é R$ {:.2f}.'.format(distância * 0.5))
else:
    print('O preço da sua passagem é R${:.2f}.'.format(distância * 0.45))
print("Tenha uma boa viagem!")

preço = distância * 0.5 if distância <= 200 else distância * 0.45

print(preço)
