from random import randrange
from time import sleep
from operator import itemgetter
dados = {}
print('Valores sorteados:')
for c in range(1, 5):
    alea = randrange(7)
    print(f'O jogador {c} tirou {alea}')
    dados[c] = alea
    sleep(1)
ranking = list()
print('Ranking dos jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: Jogador {v[0]} tirou {v[1]} ')
    sleep(1)
