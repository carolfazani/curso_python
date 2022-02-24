p1 = int(input('Digite o primeiro número: '))
p2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    opção = int(input('Escolha uma das opções: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair '))

    if opção == 1:
            soma = p1 + p2
            print(f"{p1} + {p2} = {soma}")

    elif opção == 2:
            multiplicar = p1 * p2
            print(f' {p1} x {p2} = {multiplicar}')

    elif opção == 3:
            maior = p1
            if p2 > p1:
                maior = p2
            print(f'O maior valor é {maior}')

    elif opção == 4:
        p1 = int(input('Digite o primeiro número: '))
        p2 = int(input('Digite o segundo número: '))

    elif opção == 5:
            print("Encerrando programa...")
            print('Programa finalizado')
    else:
        print('Valor inválido, tente novamente.')
