s = 0
cont = 0
for c in range(1, 500, 2):  # vai contar do 1 até 500 pulando 2 números, assim só mostra os impares.
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} números é {}'.format(cont, s))
