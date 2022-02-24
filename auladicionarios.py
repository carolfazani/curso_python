
dados = dict()
dados = {"nome": 'Carol', 'idade': 25, 'peso': 53}

print(f'O(a) {dados["nome"]} tem {dados["idade"]} anos. ')#usar aspas duplas.

dados['sexo']= 'F' #em dic n tem append, é assim q adc elementos

del dados['peso'] #apaga idade

print(dados.values()) #carol, 53..

print(dados.keys()) #nome, peso...

print(dados.items())#values + keys

for k, v in dados.items():
    print(f'O {k} é {v}.')
'''
'''
#dic em listas
brasil = [] #criei uma lista
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['sigla']) #pega a sigla do primeiro estado


#apendar
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite a Unidade Federativa: '))
    estado['estado'] = str(input('Digite o Estado: '))
    brasil.append(estado.copy())
print(brasil)

#ex 02
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')