#converter m em cm
n = float(input('Quantos metros você tem?'))
cm = n*100
m= n*1000
print('Você tem {} metros, equivalente a {} centímetros ou a {} milímetros.'.format(n, cm, m))

#tabuada
n = int(input('Digite um número: '))
tabuada = []
x = 1
while x < 11:
    resultado = n * x
    tabuada.append(resultado)
    x = x + 1
print(tabuada)

#dólar

n= float(input('Quanto dinheiro você tem? '))
dólar = n / 3.27
print(dólar)