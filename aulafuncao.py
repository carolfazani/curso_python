
def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


#(2 enters sempre entra a def e o programa principal e tem q chamar a função pra executar

título('Carol Fazani')
título('Gestora de Políticas Públicas')

#funções e tuplas
def contador(*núm): #vai passar varios parametros, * é desempacotar
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')

contador(2, 7, 8)
contador(4, 6, 8, 0)
contador(5, 7, 3, 2)

#funções e listas
def dobra (lista):
    posição = 0
    while posição < len(lista):
        lista[posição]*=2
        posição +=1

valores = [4, 6, 8, 0]
dobra(valores)
print(valores)


def soma (*valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {num}')

soma(2, 7, 8)
soma(4, 6, 8, 0)
soma(5, 7, 3, 2)

