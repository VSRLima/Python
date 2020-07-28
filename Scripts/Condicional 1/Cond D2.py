print('LEITOR DE VELOCIDADE')
print('=' * 20)
velo = float(input('Qual foi a velocidade do veiculo? '))
if velo <= 80:
    print('O veiculo estava na velocidade da via.')
    print('Tenha um bom dia!')
else:
    multa = (velo - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade de via que é 80 km/h')
    print('Sua velocidade foi {} km/h'.format(velo))
    print('A multa que você irá pagar é de R${:.2f}'.format(multa))
