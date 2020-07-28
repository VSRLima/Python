c = i = tot = 0
mais = 10
print('PROGRESSÃO ARITMÉTICA')
print('=' * 20)
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while mais != 0:
    tot += mais
    while c < tot:
        c += 1
        print(p1, end=' ')
        p1 += r
    print('PAUSA')
    mais = int(input('Quantos temros você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(tot))
