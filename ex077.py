palavras = ("Borracha", "Caderno", "Estojo",
            "Transferidor", "Compasso", "Mochila", "Canetas", "Livro")


for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')