valores = []
while True:
    continuar = 'a'
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado')
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('~' * 30)
valores.sort()
print(f'A lista é : {valores}')
