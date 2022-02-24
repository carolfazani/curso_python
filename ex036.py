valorcasa = float(input('Digite o valor do imóvel que deseja financiar: '))
salário = float(input('Digite o valor do seu salário: '))
anos = int(input('Em quantos anos deseja parcelar o imóvel? '))
prestação = valorcasa/(anos*12)

if prestação <= salário*0.3:
    print('Financiamento autorizado. O valor da sua parcela será R${:.2f} mensais. '.format(prestação))
else:
    print('Financiamento indeferido. O valor da sua parcela de R$ {:.2f} ultrapassa o valor de 30% do seu salário. '.format(prestação))
