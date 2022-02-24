peso = float(input("Digite seu peso: "))
altura = float(input('Digite sua altura: '))
IMC = peso/(altura**2)
if IMC <18.49:
    print("Seu IMC é {:.1f} e você está abaixo do peso ideal".format(IMC))
elif IMC <24.99:
    print('normal')
elif IMC <29.99:
    print('Acima do peso')
    #não terminei de colocar os indices pq fiquei com preguiça