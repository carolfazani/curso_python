from random import randint
itens = ('pedra', 'papel', 'tesoura')
usuário = (int(input('Escolha uma das opções: \n [0] pedra \n [1] papel \n [2] tesoura ')))
computador = randint(0, 2)
print('O computador escolheu {} e você escolheu {}.'.format(itens[computador], itens[usuário]))
if usuário == computador:
    print('Empate')
if usuário == 0:
    if computador == 1:
        print("Vc perdeu")
    elif computador == 2:
        print('Você ganhou')
if usuário == 1:
    if computador == 2:
        print("Vc perdeu")
    elif computador == 0:
        print('Você ganhou')
if usuário == 2:
    if computador == 0:
        print("Vc perdeu")
    elif computador == 1:
        print('Você ganhou')


