from random import randrange
maior = menor = 0
for c in range(0, 6):
    alea = randrange(11)
    tupla = (alea)
    print(tupla, end=' ')
    if c == 1 or menor > alea:
        menor = alea
    elif c == 1 or maior < alea:
        maior = alea
print(' ')
print(f'O menor valor da tupla é {menor}')
print(f'O maior valor da tupla é {maior}')
