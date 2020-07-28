from time import sleep
print('COMPARADOR DE NÚMEROS')
print('\033[32m=\033[m' * 20)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
if n1 > n2:
    print('O {} > {}!'.format(n1, n2))
elif n2 > n1:
    print('O {} > {}'.format(n2, n1))
elif n1 == n2:
    print('Os números {} e {} são \033[34miguais\033[m'.format(n1, n2))
