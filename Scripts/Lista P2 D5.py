from random import randrange
from time import sleep
print('~' * 50)
print(f'{"JOGOS NA MEGA SENA":^50}')
print('~' * 50)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for i in range(1, n + 1):
    print(f'Jogo {i}: ', end='')
    lista = list()
    for c in range(0, 6):
        r = randrange(61)
        if lista.count(r) < 1:
            lista.append(r)
    lista.sort()
    print(lista)
    sleep(1)
print('~' * 50)
