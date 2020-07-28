lista = list()
dici = dict()
jogadores = list()
while True:
    dici.clear()
    dici['Jogador'] = str(input('Digite o nome do jogador: '))
    dici['Partidas'] = int(input(f'Quantas partidas o jogador {dici["Jogador"]} jogou? '))
    lista.clear()
    for c in range(0, dici['Partidas']):
        lista.append(int(input(f'Quantos gols o jogador {dici["Jogador"]} fez na partida {c + 1}: ')))
    dici['Gols'] = lista[:]
    dici['Total'] = sum(lista)
    jogadores.append(dici.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('Cod', end=' ')
for i in dici.keys():
    print(f'{i:<10}', end='')
print()
print('~' * 45)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()
print('~' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('ERRO! O cod digitado não existe.')
    else:
        print(f'-- Levantamento do jogador {jogadores[busca]["Jogador"]}: ')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f'  No jogo {i + 1} fez {g} gols')
    print('~' * 30)
