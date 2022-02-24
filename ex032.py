from datetime import date
ano = int(input('Que ano quer analisar? Para analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {ano} é bissexto!.'.format(ano))
else:
    print('O ano {ano} não é bissexto!.'.format(ano))





