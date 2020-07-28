print('~' * 15)
print('BANCO CEV')
print('~' * 15)
dinheiro = int(input('Quanto você deseja sacar? R$'))
tot = dinheiro
c = vinte = dez = um = 0
if tot >= 50:
    while tot >= 50:
        tot -= 50
        c += 1
if tot >= 20:
    while tot >= 20:
        tot -= 20
        vinte += 1
if tot >= 10:
    while tot >= 10:
        tot -= 10
        dez += 1
if tot >= 1:
    while tot >= 1:
        tot -= 1
        um += 1
if c > 0:
    print(f'Serão dadas {c} notas de R$50.00')
if vinte > 0:
    print(f'Serão dadas {vinte} notas de R$20.00')
if dez > 0:
    print(f'Serão dadas {dez} notas de R$10.00')
if um > 0:
    print(f'Serão dadas {um} notas de R$1.00')
