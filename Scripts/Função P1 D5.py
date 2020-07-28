from random import randrange
numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randrange(11))
    print('Sorteando 5 valores da lista: ', end=' ')
    for k, v in enumerate(numeros):
        print(f'{v}', end=' ')
    print('PRONTO!')


def somapar():
    s = 0
    for c, v in enumerate(numeros):
        if v % 2 == 0:
            s += v
    print(f'A soma de todos os valores pares da lista {numeros} é {s}')


sorteia()
somapar()
