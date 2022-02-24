print('\033[1;30;41mATENÇÃO: ESSE CAIXA POSSUI APENAS CÉDULAS DE R$50, R$20, R$10 e R$1.\033[m')
notas50 = notas20 = notas10 = notas1 = 0
resto = 1
saque = int(input('Qual valor será sacado? '))
while resto > 0:
    notas50 = saque//50
    resto = saque % 50
    if resto > 0:
        notas20 = resto//20
        resto = resto % 20
        if resto > 0:
            notas10 = resto // 10
            resto = resto % 10
            if resto > 0:
                if resto > 0:
                    notas1 = resto // 1
                    resto = resto % 1

print('O caixa entregará:')
print(f'{notas50} notas de R$50' if notas50 > 0 else '')
print(f'{notas20} notas de R$20 'if notas20 > 0 else '')
print(f'{notas10} notas de R$10 ' if notas10 > 0 else '')
print(f'{notas1} notas de R$1' if notas1 > 0 else '')
