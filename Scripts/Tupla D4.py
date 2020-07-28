tupla = tuple(int(input(f'Digite {c}º valor: '))for c in range(1, 5))
print(f'Tupla: {tupla}')
print('-=' * 20)
if tupla.count(9) == 0:
    print('Não há número 9 na tupla')
else:
    print(f'Na tupla há {tupla.count(9)} números 9')
print('-=' * 20)
if tupla.count(3) == 0:
    print(f'Não há número 3 na tupla')
else:
    print(f'O número 3 está na posição {tupla.index(3) + 1}ª da tupla')
print('-=' * 20)
print('Os números pares foram:', end=' ')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
    else:
        print('0, pois não houve números pares', end='')
        break
print('.')
