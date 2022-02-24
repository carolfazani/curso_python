def voto(idade):
    if idade < 16:
        print('Proibido')
    if idade >= 16:
        print('Opcional')
    if idade >= 18:
        print('obrigatório')

i =int(input('Sua idade pf:'))
voto(idade=i)