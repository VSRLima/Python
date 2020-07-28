n = int(input('Digite um número para ver sua tabuada: '))
print('='* 25)
for c in range (1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
print('='*25)
