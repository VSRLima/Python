from math import fabs
print('Formação de triângulo')
print('=' * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero'.upper())
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não podem formar triângulos')