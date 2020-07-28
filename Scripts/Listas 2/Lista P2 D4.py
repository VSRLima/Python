lista = [[[], [], []], [[], [], []], [[], [], []]]
s = s3 = maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {i}]: '))
        lista[c][i].append(n)
        if n % 2 == 0:
            s += n
        if i == 2 and c <= 2:
            s3 += n
        if c == 1 and i <= 2:
            if n > maior:
                maior = n
print('~' * 30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'|{lista[c][i]}|', end='')
    print()
print('~' * 30)
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {maior}')
