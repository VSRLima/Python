from time import sleep
print('\033[35m=\033[m'*19)
print('\033[1;34;43mALISTAMENTO MILITAR\033[m')
print('\033[35m=\033[m'*19)
idade = int(input('Quantos anos você tem? '))
print('Em instantes você irá saber se está na hora de se alistar ou não.')
sleep(3)
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    falta = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(falta))
else:
    passou = idade - 18
    print('Você já está a {} anos atrasado para se alistar! ALISTE-SE JÁ!'.format(passou))
