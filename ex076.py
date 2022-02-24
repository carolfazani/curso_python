produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('-=-'*15)
print(f'{"LISTAGEM DE PRODUTOS":^45}')
print('-=-'*15)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<35}', end='')
    else:
        print(f'R${produtos[pos]:.2f}')
print('-=-'*15)
