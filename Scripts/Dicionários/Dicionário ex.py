'''pessoas = {'nome': 'Vinicius', 'sexo': 'M', 'idade': 20}
# del pessoas['sexo']
# pessoas['nome'] ='Leandro'
pessoas['peso'] = 98.50
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[1]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
'''for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')'''''
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
