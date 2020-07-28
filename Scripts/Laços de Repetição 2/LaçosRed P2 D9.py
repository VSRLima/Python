sn = 'S'
c = s = média = maior = menor = 0
while sn == 'S':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = s / c
print('Média {}'.format(média))
print('Maior {} e o Menor {}'.format(maior, menor))
