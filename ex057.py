'''
sexo = str(input('Digite o seu sexo [F/M]: ')).upper().strip()[0] #tudo em maiuscula, sem espaços e só a primeira letra.
while not (sexo == 'M' or sexo == 'F'):
    print('Valor inválido, digite novamente. ')
    sexo = input('Digite o seu sexo [F/M]: ').upper()
else:
    print(f'Sexo {sexo} registrado com sucesso.')

'''
sexo = str(input('Digite o seu sexo [F/M]: ')).upper().strip()[0]
while sexo not in "MmFf":
    sexo = str(input('Valor inválido. Digite o seu sexo novamente [F/M]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso.')


