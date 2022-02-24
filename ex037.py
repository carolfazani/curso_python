num = int(input('Digite um número: '))
conversão =int(input('Escolha uma opção: \n [1] Binário \n [2] Octal  \n [3] Hexadecimal'))
if conversão == 1:
    print('O valor do número {} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif conversão == 2:
    print('O valor do número {} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif conversão == 3:
    print('O valor do número {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Valor inválido. Tente novamente.')