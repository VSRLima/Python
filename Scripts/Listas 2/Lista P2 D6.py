lista = [[], [], [], []]
c = 0
while True:
    continuar = ' '
    lista[0].append(str(input('Nome: ')))
    lista[1].append(float(input('Nota 1: ')))
    lista[2].append(float(input('Nota 2: ')))
    c += 1
    print('~' * 30)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    print('~' * 30)
for i in range(0, c):
    m = (lista[1][i] + lista[2][i]) / 2
    lista[3].append(m)
print(f'{"Nº":<2} {"NOME":<15} {"MÉDIA":>5}')
for i in range(0, len(lista[0])):
    print(f'{i:<2} {lista[0][i]:<15} {lista[3][i]:>5}')
print('=' * 30)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'Notas de {lista[0][n]} são: {lista[1][n]} e {lista[2][n]}')
print('<<< VOLTE SEMPRE >>>')
