n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
if n1 > n2:
    print("O primeiro número é maior ")
elif n2 > n1:
    print('O segundo número é maior')
elif n2 == n1: #or else
    print('Os números são iguais.')
