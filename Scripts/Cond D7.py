print('Generic Eletric')
print('=' * 25)
nome = str(input('Qual o nome do funcionário? '))
sal = float(input('Qual o salário de {}? R$'.format(nome)))
if sal > 1250:
    aumentodez = ((sal * 10) / 100) + sal
    print('O salário de {} agora é {:.2f}'.format(nome, aumentodez))
else:
    aumentoquize = ((sal * 15) / 100) + sal
    print('O salário de {} agora é {:.2f}'.format(nome, aumentoquize))
