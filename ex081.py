números = []
c = 0
while True:
    números.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()
    c+=1
    if continua == 'N':
        números.sort(reverse=True)
        print(f'Você digitou {c} elementos. os valores em ordem decrescente: {números}.')
        break
if 5 in números:
    print('Olha o cinco aeee')

