preço = float(input('Qual o valor da compra? R$ '))
formadepgto = (int(input('''Qual a forma de pagamento?
[1] À vista com dinheiro
[2] À vista com cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')))
if formadepgto == 1:
    print('O valor a ser pago é de R${:.2f}.'.format(preço*0.9))
elif formadepgto == 2:
    print('O valor a ser pago é de R${:.2f}.'.format(preço*0.95))
elif formadepgto == 3:
    print('O valor a ser pago é de R${:.2f}.'.format(preço))
elif formadepgto == 4:
    print("O valor a ser pago é de R${:.2f}.".format(preço*0.8))
else:
    print('Digite uma opção válida')