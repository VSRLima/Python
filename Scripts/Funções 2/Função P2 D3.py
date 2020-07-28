def ficha(nome='', gols=''):
    if gols == '':
        gols = 0
    if gols.isnumeric():
        gols = gol
    else:
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


name = str(input('Nome do Jogador: ')).strip()
gol = str(input('Número de Gols: '))
ficha(name, gol)
