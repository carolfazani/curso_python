extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onde', 'doze', 'treze','quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    teclado= (int(input('Digite um valor: ')))
    if 0 <= teclado <=20:
        break
    print('Tente novamente!', end=' ')
print(f'Você digitou no número {extenso[teclado]}')
