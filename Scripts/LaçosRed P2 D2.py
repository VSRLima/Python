from random import randrange
from time import sleep
print('TENTE ADVINHAR QUAL É O NÚMERO DO PC')
print('=' * 25)
alea = randrange(11)
print('Acabei de pensar em um número entre 0 e 10.')
n = int(input('Qual o seu palpite? '))
c = 1
while n != alea:
    sleep(2)
    if n < alea:
        n = int(input('Mais... Tente novamente: '))
    else:
        n = int(input('Menos... Tente novamente: '))
    c += 1
print('PARABÉNS, VOCÊ ACERTOU! O número do pc foi {}'.format(alea))
print('Você precisou de {} tentativas para acertar.'.format(c))

