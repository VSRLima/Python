valores = list()
vpares = list()
vimpares = list()
while True:
    continuar = ' '
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        vpares.append(n)
    else:
        vimpares.append(n)
    valores.append(n)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {vpares}')
print(f'A lista de ímpares é: {vimpares}')
