print('PROGRESSÃO ARITMÉTICA')
print('=' * 20)
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = p1 + (11 -1) * r
for c in range(p1, decimo, r):
    print(c, end=' ')