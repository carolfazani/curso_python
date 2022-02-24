from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
idade=ano-nasc
if idade == 18:
    print('Aliste-se já!')
elif idade > 18:
    print('Seu prazo acabou!.')
else:
    print('Faltam {} anos para você se alistar. Data: {}.'.format(18-idade, nasc+18))
