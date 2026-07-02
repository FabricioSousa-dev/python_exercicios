'''pessoas = {'Nome':'Gustavo','Sexo':'M','Idade':22}
pessoas['Peso'] = 98.5
pessoas['Nome'] = 'Lendro'
del pessoas['Sexo']
print(f"O {pessoas['nome']} e do sexo {pessoas['Sexo']} e a idade é {pessoas['Idade']}")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k,v in pessoas.items():
    print(f"{k} = {v}")'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'são paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}")