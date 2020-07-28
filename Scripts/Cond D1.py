from random import randrange
from time import sleep
print('TENTE ADVINHAR QUAL NÚMERO O PC VAI COLOCAR')
print('=' * 25)
alea = randrange(11)
n = int(input('Qual é o número? '))
c = 1
while alea != n:
    print('Processando')
    sleep(2)
    if n < alea:
        n = int(input('Mais... Tente novamente: '))
    elif n > alea:
        n= int(input('Menos... Tente novamente: '))
    c += 1
print('Parabéns, você acertou! O número do PC é {}'.format(alea))
print('Você tentou {} vezes até acertar!'.format(c))
