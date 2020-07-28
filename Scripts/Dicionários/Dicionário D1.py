dici = dict()
dici['Nome'] = str(input('Nome: '))
dici['Media'] = float(input('Média: '))

if 5 <= dici['Media'] >= 7:
    dici['Situação'] = 'Aprovado'
if dici['Media'] < 7:
    dici['Situação'] = 'Recuperação'
else:
    dici['Situação'] = 'Recuperação'
print('~' * 30)
for k, v in dici.items():
    print(f'{k}: {v}')