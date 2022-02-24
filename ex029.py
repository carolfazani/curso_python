velocidade = float(input('A quantos km/h o condutor estava dirigindo? '))
if velocidade <= 80:
    pass
else:
    infração = (velocidade - 80)
    multa = (infração * 7)
    print('Limite de velocidade excedido em {}km/h. Pague uma multa no valor de R${:.2f}.'.format(infração, multa))

