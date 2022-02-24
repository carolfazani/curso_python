a = float(input('Qual altura da sua parede?'))
l = float(input('Qual a largura da sua parede? '))
ar= a*l
print('Para pintar essa parede, precisaremos de {} latas de tinta'.format(int(ar/2)))

#desconto

pi = float(input('digite o preço: R$: '))
pf = pi * 0.95
print('O valor com desconto será R$ {:.2f}'.format(pf))

#aumento de salário
sa= float(input('digite o seu salário: R$'))
ns = sa + sa * 0.15
print('Parabéns! Com o aumento seu salário mensal será de R$ {:.2f}.' .format(ns))