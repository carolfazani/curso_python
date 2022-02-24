cadastro = dict()
cadastros = list()
continua = 's'
qtde = 0
while continua in 'Ss':
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [F/M]'))
    cadastro['idade'] = int(input('Idade:'))
    cadastros.append(cadastro.copy())
    continua = str(input('Deseja continuar? [S/N]'))
    qtde += +1
idade = [cadastro['idade'] for cadastro in cadastros]
mulheres =[cadastro for cadastro in cadastros if cadastro['sexo'] in 'Ff']
média = sum(idade)/qtde
acima = [cadastro['nome'] for cadastro in cadastros if cadastro['idade'] > média]
print(f' Foram cadastradas {qtde} pessoas.')
print(f' A média de idade é {média}.')
print(f'As mulheres são{mulheres}\n.')
print(f'As pessoas acima da média são{acima}\n')



