valores = list()
while True:
    continuar = 'a'
    valores.append(int(input('Digite um valor: ')))
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(valores)}')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está presente na lista')
