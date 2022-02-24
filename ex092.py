from datetime import datetime
dados = dict()
dados['nome:'] = str(input('Nome:'))
nasc = int(input('ano de nascimento:'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Nº da CTPS:'))
if dados['ctps'] != 0:
    dados['ano_de_contratacao'] = int(input('ano de contratação:'))
    dados['salário'] = float(input('salario:'))
dados['aposentadoria'] = dados['idade'] + (dados['ano_de_contratacao'] + 35) - datetime.now().year
print(dados)