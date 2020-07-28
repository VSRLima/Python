s = p1000 = menor = c = 0
barato = ' '
while True:
    continuar = 'a'
    nome = str(input('Digite o nome do produto: ')).strip().title()
    preço = float(input('Digite o valor do produto: R$'))
    s += preço
    c += 1
    if preço > 1000:
        p1000 += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = nome
    while not continuar in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total de gastos é R${s:.2f}')
print(f'Ao todo são {p1000} produtos acima de R$1.000,00')
print(f'O produto mais barato foi {barato} por R${menor:.2f}')

