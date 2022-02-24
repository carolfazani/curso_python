números = []
continua = ' '
while continua != 'N':
    usuário = int(input('Digite um valor: '))
    if usuário in números:
        print('Valor já adicionado!')
    else:
        números.append(usuário)
        continua = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continua == 'N':
        print(f'Você digitou os valores {números}.')
        break