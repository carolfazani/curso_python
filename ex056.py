'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
mulher = 0
cont = 0
soma = 0
nomevelho = ''
maioridade = 0
for i in range(1, 5):
    print(f'---- {i}ª PESSOA ----')
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    cont += 1
    soma += idade
    if sexo == 'F' and idade < 20:
        mulher +=1
    if i==1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == "M" and maioridade < idade:
        maioridade = idade
        nomevelho = nome
print(f'A média de idade do grupo é de {soma / cont:.1f}')
print(f'O homem mais velho tem {maioridade} e se chama {nomevelho}')
print(f'{mulher} mulher(es) tem menos que 20 anos')

