from random import randint
c = 0
while True:
    usuário = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = usuário + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]:').upper().strip()[0])
    print(f'Você jogou {usuário} e o computador {computador}. A soma é {soma}.', end= '')
    print('O total é par' if soma % 2 == 0 else 'O total é impar')
    if soma % 2 == 0:
        soma = 'P'
    else:
        soma = 'I'

    if escolha == soma:
        print('Você ganhou')
        c+= +1
    if escolha != soma:
        print('Você perdeu')
        break

print(f'Fim de Jogo, você venceu {c} vezes.')
