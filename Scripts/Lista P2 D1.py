pessoas = list()
mai = men = 0
c = 0
while True:
    continuar = ' '
    nome = str(input('Nome: '))
    pessoas.append(nome)
    peso = float(input('Peso: '))
    pessoas.append(peso)
    if c == 0:
        mai = men = peso
    if peso > mai:
        mai = peso
    if peso < men:
        men = peso
    c += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continur [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Ao todo foram cadastradas {c} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for i, v in enumerate(pessoas):
    if v == mai:
        print(f'[{pessoas[i - 1]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de', end=' ')
for i, v in enumerate(pessoas):
    if v == men:
        print(f'[{pessoas[i - 1]}]', end=' ')
