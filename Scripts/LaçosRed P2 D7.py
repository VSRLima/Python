c = 3
p1 = 0
p2 = 1
print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
print('{} {}'.format(p1, p2), end=' ')
while c <= termos:
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    print('{}'.format(p3), end=' ')
    c += 1

