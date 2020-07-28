n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número:'))
if n1 > n2 and n1 > n3:
    print('O número maior é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O número maior é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número maior é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O número menor é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O número menor é {}'.format(n2))
if n3 < n1 and n3 < n1:
    print('O número menor é {}'.format(n3))
