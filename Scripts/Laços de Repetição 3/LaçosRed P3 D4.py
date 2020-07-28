print('CADASTRO DE DADOS')
print('=' * 20)
mais18 = homens = m20 = 0
while True:
    sexo = continuar = 'a'
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        mais18 += 1
    while not sexo in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade <=20 and sexo == 'F':
        m20 += 1
    print('~' * 20)
    while not continuar in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('~' * 20)
    if continuar == 'N':
        break
print(f'Foram cadastradas {mais18} pessoas maiores de 18 anos. Também {homens} homens. Por fim, {m20} mulher menor de 20 anos ')
