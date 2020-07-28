d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
dpay = d * 60
kmpay = km * 0.15
tot = dpay + kmpay
print('O total a pagar pelo carro é R${:.2f}'.format(tot))
