import math
#inteiros
'''
n = float(input("Digite um número real"))
print ('O número {} tem a parte inteira {}.'.format(n, (math.trunc(n))))

#OU 
from math import trunc
n = float(input("Digite um número real"))
print ('O número {} tem a parte inteira {}.'.format(n, trunc(n))))
#OU int(num)
'''

#hipotenusa
'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#h = math.pow(co, 2) + math.pow(ca, 2)
#print(math.sqrt(h))

#OU
h= math.hypot(co, ca)'''

#sorteio
'''import random
l= ['Maria', 'José', 'João', 'Paulo']
print(random.choice(l))
random.shuffle(l)
print(l)'''

#seno, cosseno e tangente
#from math import radians, sin, cos, tan (tirar math)
import math
a = float(input("digite o ângulo: "))
seno = math.sin(math.radians(a))
print('O ângulo de {} tem o seno de {:.2f}.'.format(a, seno))
co= math.cos(math.radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(a, co))
tan= math.tan(math.radians(a))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(a, tan))

