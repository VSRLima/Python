from math import trunc
print('Conversão Logica')
print('-=' * 15)
escolha = int(input('[1] para binário [2] para octal [3] para hexadecimal: '))
if escolha == 1:
    valor = int(input('Digite o valor desejado: '))
    print('O valor em binario é {}'.format(bin(valor)[2:]))
elif escolha == 2:
    valor = int(input('Digite o valor desejado: '))

    print('O valor em octal é {}'.format(oct(valor)[2:]))
elif escolha == 3:
    valor = int(input('Digite o valor desejado: '))
    print('O valor em hexadecimal é {}'.format(hex(valor)[2:]))
else:
    print('Opção invalida, tente novamente!')