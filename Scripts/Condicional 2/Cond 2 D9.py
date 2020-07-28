from random import choice
from time import sleep
print('\033[34m=\033[m' * 10)
print('\033[1;31;44mJOKENPÔ\033[m')
print('\033[34m=\033[m' * 10)
joke = choice(['Pedra', 'Papel', 'Tesoura'])
escolha = str(input('Escolha entre Pedra, Papel e Tesoura: ')).strip().capitalize()
print('\033[31mJO\033[m')
sleep(1)
print('\033[33mKEN\033[m')
sleep(1)
print('\033[32mPO!!!\033[m')
print('\033[33m-=\033[m' * 20)
if joke == escolha:
    print('A escolha do PC foi {}'.format(joke))
    print('\033[35mEMPATE\033[m')
elif joke == 'Pedra' and escolha == 'Papel':
    print('A escolha do PC foi {}'.format(joke))
    print('\033[36mPARABÉNS!\033[m')
elif joke == 'Papel' and escolha == 'Tesoura':
    print('A escolha do PC foi {}'.format(joke))
    print('\033[36mPARABÉNS!\033[m')
elif joke == 'Tesoura' and escolha == 'Pedra':
    print('A escolha do PC foi {}'.format(joke))
    print('\033[36mPARABÉNS!\033[m')
else:
    print('A escolha do PC foi {}'.format(joke))
    print('\033[31mVOCÊ PERDEU\033[m')
print('\033[33m-=\033[m' * 20)
