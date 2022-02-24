from datetime import date
maior = 0
menor = 0
for pessoa in range(1, 8):
    data = int(input('Digite o ano de seu nascimento: '))
    data_atual = date.today().year
    if data_atual - data <= 18:
        print('Essa pessoa é menor de idade')
        menor += 1
    else:
        print('Essa pessoa é maior de idade')
        maior += 1
print(f'Temos {maior} pessoas maiores de idade e {menor} menores de idade')