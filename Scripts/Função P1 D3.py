from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 30)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(ini, fim, passo)
