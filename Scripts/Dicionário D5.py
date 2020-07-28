lista = []
dici = dict()
s = 0
while True:
    dici.clear()
    dici['Pessoa'] = str(input('Nome: '))
    while True:
        dici['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dici['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    dici['Idade'] = int(input('Idade: '))
    s += dici['Idade']
    lista.append(dici.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo foram {len(lista)} pessoas cadastradas')
média = s / len(lista)
print(f'A média de idade é {média}')
print(f'As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Pessoa"]} ', end=' ')
print()
for i in lista:
    if i['Idade'] >= média:
        print('   ', end=' ')
        for k, v in i.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')