p1 = p2 = p3 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        p1 += +1
    if sexo == 'M':
        p2+= + 1
    if sexo == 'F' and idade < 20:
        p3+= +1
    novocadastro = ' '
    while novocadastro not in 'SN':
        novocadastro = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if novocadastro == 'N':
        break
print(f' {p1} tem mais de 18 anos. \n {p2} são homens. \n {p3} são mulheres com menos de 20 anos')
print('Fim do cadastro.')

